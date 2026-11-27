#!/usr/bin/env python3
# 使い方：python-pptx 1.0.2 入りのPythonで、台本のあるディレクトリから python3 -B pptx/build_model.py。
"""Build the seven model slides. Run with Python containing python-pptx 1.0.2."""
import sys

sys.dont_write_bytecode = True

from pptx.enum.text import PP_ALIGN
from build_common import Deck, WHITE, rect, speech, text, line


def main():
    d = Deck("model")
    c = d.c

    # 1 — Full-bleed typographic welcome; one small subordinate friend bubble.
    s = d.slide(1,
        "AIエージェントは友達です。怖くないですよ。今回はモデルの説明、ネモトロンという友達の話です。"
        "この友達は「これを探して」に答えるのが役目です。得意と不得意が分かれば、怖くなくなります。",
        "紹介／全面ティールのタイポグラフィ＋右の小さな自己紹介", cover=True)
    text(s, "AIエージェントは友達、\n怖くないよ", .75, .65, 11.8, 1.95,
         46, WHITE, True, name="manuscript title")
    text(s, "モデルの説明 —\nネモトロンという\n友達の話だよ。", .8, 3.28, 6.1, 1.80,
         28, WHITE)
    speech(s, 7.5, 3.15, 5.0, 2.35, WHITE)
    text(s, "「これを探して」に\n答えるのが、\nぼくの役目だよ", 7.86, 3.52, 4.27, 1.65,
         26, c["main"])
    text(s, "得意と不得意が分かれば、怖くなくなるよ。", .8, 6.55, 11.7, .5,
         21, WHITE)

    # 2 — An inset white speech bubble, versus unboxed limitations.
    s = d.slide(2,
        "この資料はモデルの説明です。得意と不得意が分かれば、怖くなくなります。"
        "できるのは、大量のものから探して抜き出すこと、まとめて要約すること、手順にそって手を動かすことです。"
        "最後の判断、あいまいな頼み方の読み取り、間違えないという保証はできません。"
        "人と同じで、全部できる友達はいませんし、全部できないわけでもありません。",
        "対比／左ベタ面の中の白い自己紹介吹き出し・右は面なし")
    d.title(s, 2)
    text(s, "この資料はモデルの説明だよ。\n得意と不得意が分かれば、怖くなくなるよ。",
         .68, 1.25, 11.95, .82, 19, c["ink"])
    rect(s, .65, 2.35, 6.95, 3.95, c["main"])
    text(s, "できること", .98, 2.65, 6.0, .48, 26, WHITE, True)
    speech(s, .98, 3.32, 6.27, 2.38, WHITE, tail=.20)
    text(s, "大量のものから探して、抜き出す\nまとめて、要約する\n手順にそって、手を動かす",
         1.30, 3.69, 5.63, 1.68, 23, c["main"], spacing=1.55)
    text(s, "できないこと", 8.08, 2.65, 4.55, .48, 26, c["orange"], True)
    # 項目間の余白を行間より広くし、折り返す中央の項目を一つと読めるようにする。
    for y, item, height in [
        (3.45, "最後の判断を下すこと", .48),
        (4.35, "あいまいな頼み方を\n読み取ること", .96),
        (5.65, "間違えない、という保証", .48),
    ]:
        text(s, item, 8.08, y, 4.55, height, 23, c["ink"],
             name="limitation item", spacing=1.45)
    text(s, "人と同じだよ。全部できる友達はいないし、全部できないわけでもないよ。",
         .68, 6.70, 12.0, .48, 18, c["ink"])

    # 3 — One large monologue bubble; tag overlaps its perimeter deliberately.
    s = d.slide(3,
        "ネモトロンは、こんな友達です。小さくて、とにかく速い。目がよくて、探しものが得意です。"
        "仕事場は大量のログの中。「これを探して」に答えるのが役目です。",
        "自己紹介／単一の大きな吹き出し＋名前タグ、役目だけ大きく")
    d.title(s, 3)
    speech(s, .95, 2.0, 11.42, 4.5, c["main"], tail=.28)
    rect(s, 1.40, 1.72, 2.65, .64, c["dark"], name="overlapping name tag")
    text(s, "ネモトロン", 1.58, 1.83, 2.3, .4, 22, WHITE)
    text(s, "小さくて、とにかく速い\n目がよくて、探しものが得意\n仕事場は、大量のログの中",
         1.58, 2.65, 10.12, 1.60, 26, WHITE, spacing=1.42)
    text(s, "「これを探して」に\n答えるのが役目だよ", 1.58, 4.65, 10.12, 1.38,
         34, WHITE, True)

    # 4 — Climax: wide direct-text strengths field, unboxed caveats, one close.
    s = d.slide(4,
        "探すのは得意で、つなげて考えるのは苦手です。大量のログから頼まれた行を見つけ、"
        "並べて比べ、重さや種類で仕分けます。要約して、まず大まかに分けて人へ渡します。"
        "65kを渡しても検索・抽出は保ちました。これはキミさんの実測です。"
        "一方、資料をまたぐ推論では見失いやすく、原因の連鎖は追いきれません。"
        "知らないものを知っていると思い込んだり、長い作業で目的を忘れたりします。"
        "長所も短所も友達の性格です。どちらも知っておくのが大事です。",
        "対比・山場／広い長所の直書き面と右の短所、下部に宣言済みの締め")
    d.title(s, 4, "ネモトロンは、探すのは得意で、\nつなげて考えるのは苦手だよ", 32)
    rect(s, .65, 1.90, 7.65, 4.47, c["main"])
    text(s, "長所", .98, 2.10, 6.95, .42, 26, WHITE, True)
    text(s, "探す・抜き出す", .98, 2.72, 6.95, .40, 24, WHITE, True)
    text(s, "大量のログから、頼まれた行を見つける", .98, 3.12, 6.95, .35, 19, WHITE)
    text(s, "突き合わせて仕分ける", .98, 3.61, 6.95, .40, 24, WHITE, True)
    text(s, "並べて比べて、重さや種類で分ける", .98, 4.01, 6.95, .35, 19, WHITE)
    text(s, "要約して、一次振り分け", .98, 4.50, 6.95, .40, 24, WHITE, True)
    text(s, "まず大まかに分けて、人へ渡す", .98, 4.90, 6.95, .35, 19, WHITE)
    text(s, "65k", .98, 5.52, 1.2, .58, 30, WHITE, True)
    text(s, "渡しても、検索・抽出は保った\n（キミさんの実測だよ）",
         2.38, 5.49, 5.5, .7, 18.5, WHITE)
    text(s, "短所", 8.72, 2.10, 3.95, .42, 26, c["orange"], True)
    text(s, "複数をまたぐ推論", 8.72, 2.72, 3.95, .38, 20, c["orange"], True)
    text(s, "資料をまたぐと、\n見失いやすい", 8.72, 3.10, 3.95, .61, 18, c["ink"])
    text(s, "原因の連鎖を追う", 8.72, 3.88, 3.95, .38, 20, c["orange"], True)
    text(s, "なぜそうなったかは、\n追いきれない", 8.72, 4.26, 3.95, .61, 18, c["ink"])
    text(s, "知らないものを間違える", 8.72, 5.03, 3.95, .38, 20, c["orange"], True)
    text(s, "知ってるものだと思い込む", 8.72, 5.42, 3.95, .35, 18, c["ink"])
    text(s, "長い作業では目的を忘れやすい", 8.72, 5.98, 4.15, .35, 18, c["orange"])
    text(s, "長所も短所も、この友達の性格だよ。\nどちらも知っておくのが大事だね。",
         .68, 6.57, 12.0, .80, 21, c["main"], True, name="declared bold closing")

    # 5 — Unequal horizontal flow, three large working stages and small ends.
    s = d.slide(5,
        "得意が生きる仕事を、左から見てみましょう。大量のログから、エラー時刻と該当行を探します。"
        "必要な情報だけを抜き出して並べ、重さで要約して、要る順に仕分けて渡します。"
        "人は、見るべきものから確認します。",
        "順序／小さいログと人を両端に、大きい三つの仕事を横につなぐ")
    d.title(s, 5)
    inlet = text(s, "大量の\nログ", .67, 3.19, 1.04, .90, 21, c["main"], align=PP_ALIGN.CENTER)
    a = rect(s, 2.00, 2.68, 2.35, 1.92, c["main"])
    b = rect(s, 4.75, 2.68, 2.85, 1.92, c["main"])
    cc = rect(s, 8.00, 2.68, 2.55, 1.92, c["main"])
    text(s, "探す", 2.17, 3.34, 2.01, .52, 26, WHITE, True, PP_ALIGN.CENTER)
    text(s, "抜き出して\n並べる", 4.93, 3.12, 2.49, 1.05, 25, WHITE, True, PP_ALIGN.CENTER)
    text(s, "仕分けて\n渡す", 8.18, 3.12, 2.19, 1.05, 25, WHITE, True, PP_ALIGN.CENTER)
    outlet = text(s, "人", 11.16, 3.38, 1.0, .52, 25, c["main"], align=PP_ALIGN.CENTER)
    line(s, 1.71, 3.64, 2.00, 3.64, c["main"], arrow=True, begin=inlet, end=a)
    line(s, 4.35, 3.64, 4.75, 3.64, c["main"], arrow=True, begin=a, end=b)
    line(s, 7.60, 3.64, 8.00, 3.64, c["main"], arrow=True, begin=b, end=cc)
    line(s, 10.55, 3.64, 11.16, 3.64, c["main"], arrow=True, begin=cc, end=outlet)
    text(s, "エラー時刻と\n該当行を見つける", 1.82, 4.95, 2.72, 1.0, 19, c["ink"], align=PP_ALIGN.CENTER)
    text(s, "必要な情報だけを\n取り出す", 4.68, 4.95, 2.99, 1.0, 20, c["ink"], align=PP_ALIGN.CENTER)
    text(s, "重さで要約し、\n要る順に渡す", 7.93, 4.95, 2.69, 1.0, 20, c["ink"], align=PP_ALIGN.CENTER)
    text(s, "見るべきものから\n確認する", 10.48, 4.95, 2.35, .9, 18, c["ink"], align=PP_ALIGN.CENTER)

    # 6 — Correspondence rows; the promise is a pale friend bubble, not a close.
    s = d.slide(6,
        "苦手が出る場面には、人がそばにいます。複数の資料をまたぐ判断は、人や強いモデルへ渡します。"
        "原因の連鎖を追う仕事は、人が最後まで見ます。決まった形の解析は、コードに任せます。"
        "この友達の約束は、分からないものを無理に答えず、分からないまま上げることです。",
        "対応／場面の文字とオレンジ線、渡す先の主色帯、淡い約束の吹き出し")
    d.title(s, 6)
    for y, scene, target in [
        (2.00, "複数の資料をまたぐ判断", "人や強いモデルへ渡す"),
        (3.20, "原因の連鎖を追う仕事", "人が最後まで見る"),
        (4.40, "決まった形の解析", "コードに任せる"),
    ]:
        line(s, .68, y, .68, y + .82, c["orange"], 3, name="scene caution rule")
        scene_box = text(s, scene, .94, y + .16, 5.35, .5, 25, c["ink"])
        target_shape = rect(s, 6.83, y, 5.84, .82, c["main"])
        text(s, target, 7.12, y + .18, 5.28, .5, 24, WHITE)
        line(s, 6.29, y + .41, 6.83, y + .41, c["main"], arrow=True,
             begin=scene_box, end=target_shape)
    speech(s, 2.12, 5.88, 9.10, 1.06, c["pale"], tail=.17)
    text(s, "分からないものは、無理に答えず、\n分からないまま上げるよ",
         2.50, 6.05, 8.34, .76, 21, c["main"], name="friend promise, regular weight")

    # 7 — Quiet three-line center; the transition remains a subordinate note.
    s = d.slide(7,
        "怖がらなくていいですよ。得意と不得意を知れば、ネモトロンはちゃんと役に立つ友達になります。"
        "この友達への上手な頼み方、スキルとは何かは、次のスキル編で説明します。",
        "まとめ／小さな吹き出しチップと中央の三行、次編案内は小さく下へ")
    d.title(s, 7)
    speech(s, 6.06, 1.75, 1.15, .48, c["main"], tail=.13)
    text(s, "怖がらなくていいよ。\n得意と不得意を知れば、ネモトロンは、\nちゃんと役に立つ友達になるよ。",
         1.00, 2.82, 11.33, 2.1, 31, c["main"], align=PP_ALIGN.CENTER, spacing=1.5)
    text(s, "この友達への上手な頼み方 — スキルとは何かは、\n次の資料（スキル編）で説明するよ。",
         .85, 6.00, 11.65, .88, 20, c["ink"], align=PP_ALIGN.CENTER)
    d.save()


if __name__ == "__main__":
    main()
