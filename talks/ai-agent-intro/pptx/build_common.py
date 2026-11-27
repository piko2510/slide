#!/usr/bin/env python3
# 共通描画処理。python-pptx 1.0.2 入りのPythonで python3 -B pptx/build_model.py 等から使う。
"""Shared drawing primitives; each deck assembles every page independently.

Design declaration: beginner introductions; reassuring, editable native shapes.
See ../README.md for the authoritative palette, emphasis and motifs.  Titles
and page-specific styles are read from the supplied manuscript, never invented.
"""
from datetime import datetime
from io import BytesIO
from pathlib import Path
import re
import sys
from zipfile import ZipFile

sys.dont_write_bytecode = True

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE, MSO_CONNECTOR
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.oxml.xmlchemy import OxmlElement
from pptx.util import Inches, Pt

ROOT = Path(__file__).resolve().parent.parent
FIXED_TIME = datetime(2026, 11, 27)  # UTC。OOXMLとZIPの日時を共に固定する。
FONT = "Meiryo UI"
WHITE = "FFFFFF"
PALETTES = {
    "model": dict(main="2E8B57", pale="E4F1E9", dark="1F6B41",
                  orange="DE8326", ink="23201A", bg="FFFBF8"),
    "skill": dict(main="0F6B5C", pale="DDECE7",
                  orange="C26714", ink="2B2B28", bg="FDFBF7"),
}


def rgb(value):
    return RGBColor.from_string(value)


def font_xml(rpr, size, color, bold=False, strike=False):
    rpr.set("sz", str(round(size * 100)))
    rpr.set("b", "1" if bold else "0")
    if strike:
        rpr.set("strike", "sngStrike")
    for tag in ("latin", "ea", "cs"):
        child = rpr.find(f"{{http://schemas.openxmlformats.org/drawingml/2006/main}}{tag}")
        if child is None:
            child = OxmlElement(f"a:{tag}")
            rpr.append(child)
        child.set("typeface", FONT)


def no_shadow(shape):
    sppr = shape._element.spPr
    for old in list(sppr):
        if old.tag.rsplit("}", 1)[-1] in ("effectLst", "effectDag"):
            sppr.remove(old)
    # An explicit empty list overrides the shadow inherited from the theme.
    sppr.append(OxmlElement("a:effectLst"))
    # Impress also consults effectRef even when effectLst is empty.
    for ref in shape._element.xpath("./p:style/a:effectRef"):
        ref.set("idx", "0")


def rect(slide, x, y, w, h, fill=None, line=None, line_width=1.5,
         name="panel", ellipse=False):
    shape = slide.shapes.add_shape(
        MSO_SHAPE.OVAL if ellipse else MSO_SHAPE.RECTANGLE,
        Inches(x), Inches(y), Inches(w), Inches(h))
    shape.name = name
    if fill:
        shape.fill.solid()
        shape.fill.fore_color.rgb = rgb(fill)
    else:
        shape.fill.background()
    if line:
        shape.line.color.rgb = rgb(line)
        shape.line.width = Pt(line_width)
    else:
        shape.line.fill.background()
    no_shadow(shape)
    return shape


def speech(slide, x, y, w, h, fill, name="friend speech", tail=.22):
    """Single editable native freeform, with a restrained bottom-left tail."""
    vertices = [(0, 0), (w, 0), (w, h), (.85, h),
                (.52, h + tail), (.52, h), (0, h)]
    builder = slide.shapes.build_freeform(Inches(x), Inches(y), 1.0)
    builder.add_line_segments([(Inches(x + a), Inches(y + b))
                               for a, b in vertices[1:]], close=True)
    shape = builder.convert_to_shape()
    shape.name = name
    shape.fill.solid()
    shape.fill.fore_color.rgb = rgb(fill)
    shape.line.fill.background()
    no_shadow(shape)
    return shape


def text(slide, content, x, y, w, h, size, color, bold=False,
         align=PP_ALIGN.LEFT, strike=False, name=None, spacing=1.16):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    box.name = name or "text: " + content.replace("\n", " ")[:45]
    tf = box.text_frame
    tf.clear()
    tf.margin_left = tf.margin_right = 0
    tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.TOP
    tf.auto_size = MSO_AUTO_SIZE.NONE
    tf.word_wrap = False
    for i, line in enumerate(content.split("\n")):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        p.space_before = Pt(0)
        p.space_after = Pt(0)
        p.line_spacing = spacing
        r = p.add_run()
        r.text = line
        r.font.name = FONT
        r.font.size = Pt(size)
        r.font.bold = bold
        r.font.color.rgb = rgb(color)
        font_xml(r._r.get_or_add_rPr(), size, color, bold, strike)
    no_shadow(box)
    return box


def line(slide, x1, y1, x2, y2, color, width=2, arrow=False,
         name="connector", begin=None, end=None, begin_idx=3, end_idx=1):
    shape = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT,
                                      Inches(x1), Inches(y1),
                                      Inches(x2), Inches(y2))
    shape.name = name
    shape.line.color.rgb = rgb(color)
    shape.line.width = Pt(width)
    if begin is not None:
        shape.begin_connect(begin, begin_idx)
    if end is not None:
        shape.end_connect(end, end_idx)
    if arrow:
        end_tag = OxmlElement("a:tailEnd")
        end_tag.set("type", "triangle")
        end_tag.set("w", "sm")
        end_tag.set("len", "sm")
        shape._element.spPr.get_or_add_ln().append(end_tag)
    no_shadow(shape)
    return shape


def checkline(slide, x, centers, c, fill=None, branches_to=None):
    """Numbered circles and native check strokes joined by primary-color lines."""
    radius = .22
    for a, b in zip(centers, centers[1:]):
        line(slide, x, a + radius, x, b - radius, c, 2.1,
             name="checkline spine")
        mid = (a + b) / 2
        line(slide, x - .10, mid, x - .025, mid + .075, c, 2.4,
             name="check left stroke")
        line(slide, x - .025, mid + .075, x + .13, mid - .10, c, 2.4,
             name="check right stroke")
    for n, cy in enumerate(centers, 1):
        rect(slide, x - radius, cy - radius, 2 * radius, 2 * radius,
             fill or c, c, name=f"step {n}", ellipse=True)
        text(slide, str(n), x - radius, cy - .175, 2 * radius, .35,
             18, c if fill else WHITE, True, PP_ALIGN.CENTER)
        if branches_to is not None:
            line(slide, x + radius, cy, branches_to, cy, c, 2,
                 name="checkline row connection")


def sections(deck):
    supplied = (ROOT / f"{deck}.md").read_text()
    chunks = re.split(r"^## (\d+)\. (.+)$", supplied, flags=re.M)
    return [(chunks[i + 1], chunks[i + 2].strip())
            for i in range(1, len(chunks), 3)]


class Deck:
    def __init__(self, kind):
        self.kind = kind
        self.c = PALETTES[kind]
        self.source = sections(kind)
        self.prs = Presentation()
        self.prs.slide_width = Inches(13.333)
        self.prs.slide_height = Inches(7.5)
        self.prs.core_properties.title = (
            "AIエージェント入門 — モデル編" if kind == "model" else
            "AIエージェント入門 — スキル編")
        self.prs.core_properties.author = ""
        self.prs.core_properties.created = FIXED_TIME
        self.prs.core_properties.modified = FIXED_TIME
        self.prs.core_properties.subject = "台本準拠・ネイティブ図形"

    def slide(self, number, spoken, layout, cover=False):
        slide = self.prs.slides.add_slide(self.prs.slide_layouts[6])
        slide.background.fill.solid()
        slide.background.fill.fore_color.rgb = rgb(
            self.c["main"] if cover else self.c["bg"])
        strength = (("強く" if self.kind == "skill" else "迎える強さ")
                    if number == 1 else "静かに閉じる" if number == 7
                    else "山場" if number == (4 if self.kind == "model" else 6)
                    else "中")
        style = re.search(r"^様式：(.*)$", self.source[number - 1][1], re.M).group(1)
        tones = f"淡色 #{self.c['pale']}"
        if self.kind == "model":
            tones += f"・濃色 #{self.c['dark']}"
        tech = (
            f"色：主色 #{self.c['main']}、{tones}（同系統で1色）。"
            f"アクセント #{self.c['orange']} は"
            f"できないこと・短所・注意のみ。中立色 #{self.c['ink']}、背景 #{self.c['bg']}。"
            "白は反転文字・白面。主色の視覚の重さはデッキ全体で60〜70％を目安。\n"
            f"強弱：{strength}。関係と型：{layout}。\n様式の正本：{style}\n"
            "生成：python-pptxによるネイティブ経路。テキスト・図形・コネクタは編集可能。"
            "フォント：Meiryo UI（latin・東アジアを明示）。影なし。"
            "描画はNoto Sans CJK JPの代替で、PowerPoint実機の表示は未確認。"
        )
        if self.kind == "model" and number == 4:
            tech += "\n65kはキミさん本人の実測であり、一般的な性能保証ではない。"
        notes_tf = slide.notes_slide.notes_text_frame
        notes_tf.text = f"【話す内容】\n{spoken}\n\n【技術注記】\n{tech}"
        for shape in slide.notes_slide.shapes:
            if shape.has_text_frame:
                for p in shape.text_frame.paragraphs:
                    for r in p.runs:
                        r.font.name = FONT
                        r.font.size = Pt(18)
                        font_xml(r._r.get_or_add_rPr(), 18, self.c["ink"])
        return slide

    def title(self, slide, number, lines=None, size=32):
        content = lines or self.source[number - 1][0]
        assert content.replace("\n", "") == self.source[number - 1][0]
        return text(slide, content, .65, .40, 12.03, 1.2,
                    size, self.c["main"], True, name="manuscript title")

    def save(self):
        path = ROOT / f"ai-agent-intro-{self.kind}.pptx"
        package = BytesIO()
        self.prs.save(package)
        # python-pptxのZIP格納日時も揃え、同じ入力を同じバイト列にする。
        with ZipFile(package) as source, ZipFile(path, "w") as target:
            for info in source.infolist():
                info.date_time = FIXED_TIME.timetuple()[:6]
                target.writestr(info, source.read(info.filename))
        print(f"Created {path.relative_to(ROOT)} ({len(self.prs.slides)} slides)")
