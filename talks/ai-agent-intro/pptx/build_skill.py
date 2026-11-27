#!/usr/bin/env python3
# 使い方：python-pptx 1.0.2 入りのPythonで、台本のあるディレクトリから python3 -B pptx/build_skill.py。
"""Build the seven skill slides with page-specific native compositions."""
import sys

sys.dont_write_bytecode = True

from pptx.enum.text import PP_ALIGN
from build_common import Deck, WHITE, rect, text, line, checkline


def main():
    d = Deck("skill")
    c = d.c

    # 1 — Full-bleed welcome; a white skill card between two text-only actors.
    s = d.slide(1,
        "スキルとは何でしょうか。モデルを変えずに、頼み方を決める手順書の話です。"
        "頼む人が仕事を頼み、スキルに探すもの、返す形、分からないときを書き、モデルが仕事をします。"
        "この資料はスキルの説明だけです。モデルの説明は前の資料です。",
        "順序・表紙／白いスキルカードを主役に、両端は文字だけ", cover=True)
    text(s, "スキルとはなにか", .75, .60, 11.8, 1.0, 50, WHITE, True, name="manuscript title")
    text(s, "モデルを変えずに、頼み方を決める手順書の話。", .8, 1.82, 11.7, .62, 26, WHITE)
    card = rect(s, 4.03, 3.00, 5.10, 2.96, WHITE, name="white skill card")
    text(s, "頼む人", .75, 3.88, 2.4, .56, 29, WHITE, align=PP_ALIGN.CENTER)
    text(s, "（仕事を頼む）", .75, 4.55, 2.4, .45, 19, WHITE, align=PP_ALIGN.CENTER)
    text(s, "スキル", 4.45, 3.23, 4.25, .56, 30, c["main"], True)
    text(s, "頼み方の手順書", 4.45, 3.91, 4.25, .45, 23, c["main"])
    text(s, "✓ 探すもの\n✓ 返す形\n✓ 分からないとき", 4.45, 4.47, 4.25, 1.24,
         23, c["main"], spacing=1.18)
    text(s, "モデル", 10.13, 3.88, 2.4, .56, 29, WHITE, align=PP_ALIGN.CENTER)
    text(s, "（仕事をする）", 10.13, 4.55, 2.4, .45, 19, WHITE, align=PP_ALIGN.CENTER)
    line(s, 3.27, 4.48, 4.03, 4.48, WHITE, arrow=True, end=card)
    line(s, 9.13, 4.48, 9.90, 4.48, WHITE, arrow=True, begin=card)
    text(s, "この資料は、スキルの説明だけをします。モデルの説明は、前の資料です。",
         .8, 6.75, 11.7, .45, 18, WHITE)

    # 2 — Explanatory prose and one solid manual, whose content is a checkline.
    s = d.slide(2,
        "スキルは、モデルを変えずに頼み方を決める手順書です。料理のレシピや仕事の手順書のようなものです。"
        "書いてあるので、頼むたびに説明し直さなくていい。友達そのものではなく、友達への頼み方のメモです。"
        "書くのは、探すものは何か、返す形はどうするか、分からないときどう言うか。"
        "レシピや作業マニュアルと同じです。同じ頼み方をすれば、毎回同じ進め方になります。",
        "説明と内容／左の文章・右のベタ面手順書パネル内にチェック線")
    d.title(s, 2, "スキルは、モデルを変えずに\n「頼み方」を決める手順書だ")
    text(s, "たとえば、料理のレシピや\n仕事の手順書のようなもの。\n書いてあるから、頼むたびに\n説明し直さなくていい。\n友達そのものではなく、\n友達への頼み方のメモだよ。",
         .68, 2.22, 5.16, 3.55, 24, c["ink"], spacing=1.35)
    rect(s, 6.27, 1.98, 6.40, 3.98, c["main"])
    text(s, "手順書に書くこと", 6.63, 2.22, 5.65, .50, 26, WHITE, True)
    rect(s, 6.60, 2.98, .70, 2.55, c["pale"], name="checkline inset")
    checkline(s, 6.95, [3.30, 4.18, 5.06], c["main"], fill=WHITE)
    text(s, "探すものは何か", 7.65, 3.08, 4.65, .48, 24, WHITE)
    text(s, "返す形はどうするか", 7.65, 3.96, 4.65, .48, 24, WHITE)
    text(s, "分からないとき、\nどう言うか", 7.65, 4.78, 4.65, .9, 24, WHITE)
    text(s, "レシピや作業マニュアルと同じです。\n同じ頼み方をすれば、毎回同じ進め方になります。",
         .8, 6.35, 11.7, .82, 19, c["ink"])

    # 3 — Moderate side-by-side distinction, outlined model and solid skill.
    s = d.slide(3,
        "モデルとスキルは役割が違います。モデルは友達そのもの。できることと、できないことが、ここで決まります。"
        "スキルは頼み方の手順書。頼み方と進め方が、ここで決まります。"
        "スキルを書いても、できないことができるようにはなりません。",
        "対比／段違いの定義面、モデル見出しは面の外・スキル見出しは面の中、間に≠")
    d.title(s, 3)
    rect(s, .68, 2.97, 4.55, 2.80, line=c["main"], line_width=2)
    text(s, "モデル", .98, 2.12, 3.95, .56, 29, c["main"], True)
    text(s, "友達そのもの。\nできることと、\nできないことが、\nここで決まる", 1.03, 3.32, 3.85, 2.0, 24, c["ink"], spacing=1.30)
    text(s, "≠", 5.57, 3.47, 1.0, .85, 46, c["main"], align=PP_ALIGN.CENTER)
    rect(s, 7.00, 1.98, 5.65, 3.79, c["main"])
    text(s, "スキル", 7.40, 2.40, 4.85, .56, 29, WHITE, True)
    text(s, "頼み方の手順書。\n頼み方と、進め方が、\nここで決まる", 7.40, 3.42, 4.85, 1.8, 25, WHITE, spacing=1.30)
    text(s, "注意：スキルを書いても、できないことが、\nできるようにはなりません。",
         .8, 6.25, 11.7, .90, 21, c["orange"])

    # 4 — The orange bad request dominates; unequal destinations underneath.
    s = d.slide(4,
        "できないことは、無理にお願いしません。「原因を特定して、直して」という頼み方は避けます。"
        "短所に当たらないように、仕事を分けて渡します。解析はコードへ。決まった処理は機械的に行います。"
        "探すこと、仕分けることはモデルへ。得意な仕事だけを渡します。"
        "最終判断は人や強いモデルへ。責任がいる判断はこちらです。",
        "注意と分担／上の大きなオレンジ面＋下の不均等な三列、モデル列のみベタ面")
    d.title(s, 4)
    rect(s, .65, 1.60, 12.03, 1.72, c["orange"], name="dominant bad request")
    text(s, "悪い頼み方", .97, 1.80, 11.35, .44, 23, WHITE)
    text(s, "「原因を特定して、直して」", .97, 2.29, 11.35, .70, 34, WHITE, True,
         strike=True)
    text(s, "短所に当たらないように、仕事を分けて渡します。", .8, 3.65, 11.7, .52, 23, c["ink"])
    rect(s, 3.55, 4.40, 4.90, 2.55, c["main"], name="subordinate model destination")
    code_job = text(s, "解析する", .82, 4.52, 2.05, .45, 23, c["main"], True)
    code_target = text(s, "コードへ", .82, 5.48, 2.05, .48, 24, c["main"], True)
    line(s, 1.845, 4.97, 1.845, 5.48, c["main"], arrow=True,
         begin=code_job, end=code_target, begin_idx=2, end_idx=0)
    text(s, "決まった処理は\n機械的に", .82, 6.13, 2.25, .73, 19, c["ink"])
    model_job = text(s, "探す・仕分ける", 3.94, 4.52, 4.12, .45, 24, WHITE, True)
    model_target = text(s, "モデルへ", 3.94, 5.48, 4.12, .5, 27, WHITE, True)
    line(s, 6.0, 4.97, 6.0, 5.48, WHITE, arrow=True,
         begin=model_job, end=model_target, begin_idx=2, end_idx=0)
    text(s, "得意な仕事だけを渡す", 3.94, 6.20, 4.12, .45, 20, WHITE)
    human_job = text(s, "最終判断", 9.18, 4.52, 3.40, .45, 23, c["main"], True)
    human_target = text(s, "人・強いモデルへ", 9.18, 5.48, 3.40, .48, 23, c["main"], True)
    line(s, 10.88, 4.97, 10.88, 5.48, c["main"], arrow=True,
         begin=human_job, end=human_target, begin_idx=2, end_idx=0)
    text(s, "責任がいる判断は\nこちら", 9.18, 6.13, 3.40, .73, 19, c["ink"])

    # 5 — The numbered/check spine is the layout, not a repeated title motif.
    s = d.slide(5,
        "長所を伸ばす書き方をしましょう。一つ目は、探すものを書くこと。例はエラー時刻と該当する行です。"
        "二つ目は、返す形を書くこと。例は時刻の順に並べて渡すことです。"
        "三つ目は、分からないときの言い方を書くこと。例は「分からない」と書くことです。"
        "四つ目は、仕事を一回に一つだけにすること。探すことと仕分けることは分けます。",
        "順序／番号丸をつなぐチェック線から四つの記述へ、単一の主色面")
    d.title(s, 5, "長所を伸ばす書き方をすると、\n得意な仕事が返ってくる")
    rect(s, 1.72, 1.98, 10.95, 4.90, c["main"], name="single writing field")
    checkline(s, 1.07, [2.45, 3.60, 4.75, 5.90], c["main"], branches_to=1.72)
    text(s, "探すものを書く", 2.08, 2.19, 10.20, .45, 25, WHITE, True)
    text(s, "例：エラー時刻と、該当する行", 2.08, 2.72, 10.20, .42, 20, WHITE)
    text(s, "返す形を書く", 2.08, 3.34, 10.20, .45, 25, WHITE, True)
    text(s, "例：時刻の順に並べて渡す", 2.08, 3.87, 10.20, .42, 20, WHITE)
    text(s, "分からないときの言い方を書く", 2.08, 4.49, 10.20, .45, 25, WHITE, True)
    text(s, "例：「分からない」と書く", 2.08, 5.02, 10.20, .42, 20, WHITE)
    text(s, "仕事は1回に1つだけにする", 2.08, 5.64, 10.20, .45, 25, WHITE, True)
    text(s, "例：探す、と仕分ける、は分ける", 2.08, 6.17, 10.20, .42, 20, WHITE)

    # 6 — Climax: asymmetrical quote comparison, a much larger concrete side.
    s = d.slide(6,
        "頼み方を具体的にすると、答えが使えるものになります。「ログを見ておいて」では、"
        "何を探すかが決まらず、答えが毎回ぶれます。"
        "「エラー時刻と該当行を抜いて、重さで仕分けて。分からないものは『分からない』と書いて」"
        "なら、探すものと返す形が決まっています。"
        "書くのは、探すもの、返す形、分からないときの言い方、仕事は一つ、この四点です。",
        "対比・山場／あいまい側は引用だけ小さい輪郭枠、具体側は説明まで含む大きなベタ面")
    d.title(s, 6, "頼み方を具体的にすると、\n答えが使えるものになる")
    rect(s, .65, 3.02, 3.70, 1.57, line=c["orange"], line_width=2,
         name="small vague quotation outline")
    text(s, "あいまいな頼み方", .96, 2.30, 3.10, .48, 24, c["orange"], True)
    text(s, "「ログを\n見ておいて」", .96, 3.15, 3.10, 1.15, 28, c["ink"])
    text(s, "何を探すのかが\n決まらず、答えが\n毎回ぶれます", .96, 4.85, 3.10, 1.2, 20, c["ink"], spacing=1.35)
    rect(s, 4.85, 1.98, 7.82, 4.52, c["main"])
    text(s, "具体的な頼み方", 5.23, 2.30, 7.06, .48, 25, WHITE, True)
    text(s, "「エラー時刻と該当行を\n抜いて、重さで仕分けて。\n分からないものは\n『分からない』と書いて」",
         5.23, 3.15, 7.06, 2.10, 27, WHITE, spacing=1.30)
    text(s, "探すものと返す形が、決まっている", 5.23, 5.70, 7.06, .52, 21, WHITE)
    text(s, "書くのはこの4点だけです。\n探すもの、返す形、分からないときの言い方、仕事は1つ。",
         .8, 6.72, 11.7, .70, 18, c["ink"])

    # 7 — Quiet three-bullet checkline; introductory/final prose stays secondary.
    s = d.slide(7,
        "スキルは魔法ではありません。得意が生きる頼み方を書いて残すものです。"
        "短所は隠さず、当たらないように仕事を分けます。長所は伸ばします。"
        "探すもの、返す形、分からないときの言い方を書きます。頼み方は残します。"
        "書いて残せば、他の人も同じように頼めます。できないことは頼まず、得意な頼み方をする。"
        "それだけで、友達はちゃんと役に立ちます。",
        "まとめ／チェック線につながる三つの箇条、前置きと最後の文は補足の強さ")
    d.title(s, 7)
    text(s, "スキルは魔法ではない。\n得意が生きる頼み方を、書いて残すものだ。",
         .8, 1.36, 11.7, .95, 20, c["ink"])
    checkline(s, 1.08, [3.10, 4.28, 5.46], c["main"])
    text(s, "短所は、隠さない", 1.85, 2.86, 3.7, .48, 24, c["main"], True)
    text(s, "当たらないように、仕事を分ける", 5.57, 2.91, 7.03, .45, 20, c["ink"])
    text(s, "長所は、伸ばす", 1.85, 4.04, 3.7, .48, 24, c["main"], True)
    text(s, "探すもの・返す形・\n分からないときの言い方を書く", 5.57, 3.99, 7.03, .85, 20, c["ink"])
    text(s, "頼み方は、残す", 1.85, 5.22, 3.7, .48, 24, c["main"], True)
    text(s, "書いて残せば、他の人も\n同じように頼める", 5.57, 5.17, 7.03, .85, 20, c["ink"])
    text(s, "できないことは頼まない。得意な頼み方をする。\nそれだけで、友達はちゃんと役に立つ。",
         .8, 6.62, 11.7, .80, 18.5, c["ink"])
    d.save()


if __name__ == "__main__":
    main()
