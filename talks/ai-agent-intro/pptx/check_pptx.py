#!/usr/bin/env python3
# 使い方：python-pptx 1.0.2 入りのPythonで生成後、python3 -B pptx/check_pptx.py で台本とPPTXを検査。
"""Inspect the saved OOXML, rather than relying on generator defaults."""
from pathlib import Path
import re
import sys
sys.dont_write_bytecode = True
from zipfile import ZipFile
from lxml import etree

ROOT = Path(__file__).resolve().parent.parent
NS = {"a": "http://schemas.openxmlformats.org/drawingml/2006/main",
      "p": "http://schemas.openxmlformats.org/presentationml/2006/main"}


def normalized(text):
    return re.sub(r'[\s：:—→／✓（）「」『』。、・,.\-]', '', text)


def source_check(deck, slides):
    """Check all source phrases, ignoring only markup and layout instructions."""
    source = (ROOT / f"{deck}.md").read_text()
    chunks = re.split(r"^## (\d+)\. (.+)$", source, flags=re.M)
    expected = [(chunks[i + 1], chunks[i + 2].strip())
                for i in range(1, len(chunks), 3)]
    failures, phrase_count, title_count = [], 0, 0
    for i, ((title, body), root) in enumerate(zip(expected, slides), 1):
        actual = normalized("".join(root.xpath(".//a:t/text()", namespaces=NS)))
        if normalized(title) in actual:
            title_count += 1
        else:
            failures.append(f"{deck} slide {i}: missing title {title}")
        for line in body.splitlines():
            if not line.strip() or line.startswith("様式："):
                continue
            line = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', line)
            line = re.sub(r'（(?:大きく|取り消し線|オレンジ)）', '', line)
            line = re.sub(r'^吹き出し（友達の自己紹介）：', '', line)
            line = re.sub(r'^(?:締め|帯)：', '', line)
            line = re.sub(r'^(?:- |\d+\. )', '', line)
            for piece in re.split(r'：|—|→|／|✓|（|）', line):
                phrase = normalized(piece)
                if phrase:
                    phrase_count += 1
                    if phrase not in actual:
                        failures.append(f"{deck} slide {i}: missing phrase {piece}")
    if len(expected) != 7 or len(slides) != 7:
        failures.append(f"{deck}: source/slide count is not seven")
    print(f"{deck}: source phrases={phrase_count}; missing={len(failures)}; titles={title_count}/7")
    return failures


def inspect(path, deck):
    rows, errors = [], []
    with ZipFile(path) as z:
        prs = etree.fromstring(z.read("ppt/presentation.xml"))
        slide_paths = sorted([n for n in z.namelist()
                              if re.fullmatch(r"ppt/slides/slide\d+\.xml", n)],
                             key=lambda n: int(re.search(r"(\d+)\.xml", n).group(1)))
        count_ok = len(slide_paths) == 7 and len(prs.findall("p:sldIdLst/p:sldId", NS)) == 7
        dim = prs.find("p:sldSz", NS)
        size_ok = (dim.get("cx"), dim.get("cy")) == ("12191695", "6858000")
        print(f"{deck}: slides={len(slide_paths)} (expected 7); "
              f"size=13.333 x 7.5 in: {'PASS' if size_ok else 'FAIL'}")
        if not count_ok or not size_ok:
            errors.append(f"{deck}: slide count or dimensions")
        slide_roots = []
        for i, name in enumerate(slide_paths, 1):
            root = etree.fromstring(z.read(name))
            slide_roots.append(root)
            pictures = len(root.findall(".//p:pic", NS))
            notes = etree.fromstring(z.read(f"ppt/notesSlides/notesSlide{i}.xml"))
            note_text = "".join(notes.xpath(".//a:t/text()", namespaces=NS))
            slide_runs = root.findall(".//a:r", NS)
            # Notes have the same font requirements as displayed text.
            runs = slide_runs + notes.findall(".//a:r", NS)
            latin = ea = sized = True
            sizes = []
            for run in runs:
                rp = run.find("a:rPr", NS)
                lat = None if rp is None else rp.find("a:latin", NS)
                east = None if rp is None else rp.find("a:ea", NS)
                latin &= lat is not None and lat.get("typeface") == "Meiryo UI"
                ea &= east is not None and east.get("typeface") == "Meiryo UI"
                sz = 0 if rp is None else int(rp.get("sz", "0"))
                sized &= sz >= 1800
                sizes.append(sz / 100)
            headings = all(h in note_text for h in ("【話す内容】", "【技術注記】"))
            autofit = len(root.findall(".//a:normAutofit", NS)) == 0
            shadow = not root.xpath(
                ".//a:outerShdw | .//a:innerShdw | .//a:effectRef[@idx!='0']", namespaces=NS)
            explicit_effects = all(sp.find("a:effectLst", NS) is not None
                                   for sp in root.findall(".//p:spPr", NS))
            bounds = True
            for xfrm in root.findall(".//a:xfrm", NS):
                off, ext = xfrm.find("a:off", NS), xfrm.find("a:ext", NS)
                if off is not None and ext is not None:
                    x, y = int(off.get("x")), int(off.get("y"))
                    w, h = int(ext.get("cx")), int(ext.get("cy"))
                    bounds &= x >= 0 and y >= 0 and x + w <= 12191695 and y + h <= 6858000
            ok = bool(runs) and all([count_ok, size_ok, pictures == 0, latin, ea,
                                    sized, headings, autofit, shadow, explicit_effects, bounds])
            rows.append([deck, str(i), str(pictures), str(len(slide_runs)),
                         "OK" if latin else "FAIL", "OK" if ea else "FAIL",
                         f"{min(sizes):g}" if sizes else "none",
                         "OK" if headings else "FAIL", "OK" if autofit else "FAIL",
                         "OK" if shadow and explicit_effects else "FAIL",
                         "OK" if bounds else "FAIL", "PASS" if ok else "FAIL"])
            if not ok:
                errors.append(f"{deck} slide {i}: " + ", ".join(
                    n for n, value in [("pictures", pictures == 0), ("latin", latin),
                    ("ea", ea), ("size", sized), ("notes", headings),
                    ("autofit", autofit), ("shadow", shadow and explicit_effects),
                    ("bounds", bounds)] if not value))
        errors.extend(source_check(deck, slide_roots))
    return rows, errors


def main():
    rows, errors = [], []
    for deck in ("model", "skill"):
        try:
            result, failures = inspect(ROOT / f"ai-agent-intro-{deck}.pptx", deck)
            rows.extend(result)
            errors.extend(failures)
        except Exception as exc:
            errors.append(f"{deck}: {type(exc).__name__}: {exc}")
    print("| deck | page | picture | runs | latin | ea | min pt* | notes | no shrink | no shadow | bounds | result |")
    print("|---|---:|---:|---:|---|---|---:|---|---|---|---|---|")
    for row in rows:
        print("| " + " | ".join(row) + " |")
    print("* min pt includes notes; latin/ea/size checks cover slide and note runs.")
    for error in errors:
        print("ERROR: " + error)
    print(f"Overall: {'FAIL' if errors else 'PASS'} ({len(rows)} pages)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
