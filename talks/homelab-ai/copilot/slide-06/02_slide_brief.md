# 第06枚の制作仕様

出力：homelab_ai_06.pptx、1枚のみ、45秒のページ。
以下の共通styleと当該ページの表だけで単独生成できる。説明文は画面に出さない。

## 共通制作style

この文書は制作指示であり、スライドへ転載しない。画面に出す文字は各ページのobject表のtext種別のText欄だけを正本とする。rect種別のText空欄は無文字を意味する。<br>は明示改行であり文字列として表示しない。Unicodeの矢印文字を作らず、接続線表どおりの編集可能なPowerPointコネクタを作る。

- キャンバス：960 × 540 pt（13.3333 × 7.5 inch、16:9）。原点は左上。1 pt = 12700 EMU、72 pt = 1 inch。
- 背景：白 #FFFFFF。すべての文字のLatinとEast Asianフォント名をMeiryo UIへ設定する。
- 色：本文 #222222、補足 #505050、青 #1F5FAF、薄灰 #F5F6F8、枠 #D0D5DD。
- 外周余白：左40 pt、右40 pt、上28 pt、下28 pt。ページ番号だけはy=498..512 pt。通常のtitleはy=28..76 pt、主図はy=100..450 pt、注記はy=470..498 ptに置く。
- オブジェクト座標はx,y,w,hの順にpt。四角の角丸は0、影なし。zが小さいものから描く。すべての文字を別のテキストボックスとし、背景の四角に文字を入れない。
- テキストは自動縮小、自動拡張、均等割付をOFF。指定の明示改行だけを使う。行が収まらない場合は原因を特定し、制作者が文字サイズを下げたり文言を追加したりしない。
- テキスト枠の内余白は上下左右0。行間は次の表の倍率、段落前後は0。垂直位置は中央。ここにないフォント、色、塗り、線、配置を推測して加えない。
- line表のsource/targetはshapeID:辺@割合。辺の割合は左上から右下へ0..1。source境界座標→waypoint→target境界座標の各隣接点を、個別の直線PowerPointコネクタとして作る。本数は点列長-1で、IDは論理ID_s1、_s2の順。矢印headは最後のsegmentのtarget側だけに付ける。sourceとtargetの箱の境界座標を保ち、自動ルーティングは使わない。Segment表の座標が描画の正本。コネクタはz=20で背景の上、文字の下。文字や無関係な内容パネルを貫通させない。
- 本編は13枚、計600秒。出力は指定ページ1枚だけの編集可能な.pptx。PPTXへ画像化せず、写真、ロゴ、家や雲の装飾輪郭、グラデーション、影を加えない。

| Style | 種別 | フォントとpt | 太さ | 文字色 | 塗り | 枠線 | 内余白（上/右/下/左、pt） | 水平/垂直 | 行間 |
|---|---|---|---|---|---|---|---|---|---|
| T32 | text | Meiryo UI 32 | bold | #222222 | なし | なし | 0/0/0/0 | 左/中央 | 1.00 |
| T40 | text | Meiryo UI 40 | bold | #222222 | なし | なし | 0/0/0/0 | 左/中央 | 1.00 |
| B28 | text | Meiryo UI 28 | bold | #222222 | なし | なし | 0/0/0/0 | 左/中央 | 1.05 |
| B24 | text | Meiryo UI 24 | regular | #222222 | なし | なし | 0/0/0/0 | 左/中央 | 1.08 |
| B22 | text | Meiryo UI 22 | regular | #222222 | なし | なし | 0/0/0/0 | 左/中央 | 1.10 |
| C22 | text | Meiryo UI 22 | regular | #222222 | なし | なし | 0/0/0/0 | 中央/中央 | 1.10 |
| L20 | text | Meiryo UI 20 | bold | #1F5FAF | なし | なし | 0/0/0/0 | 左/中央 | 1.00 |
| C20 | text | Meiryo UI 20 | bold | #1F5FAF | なし | なし | 0/0/0/0 | 中央/中央 | 1.00 |
| E24 | text | Meiryo UI 24 | bold | #1F5FAF | なし | なし | 0/0/0/0 | 左/中央 | 1.05 |
| N14 | text | Meiryo UI 14 | regular | #505050 | なし | なし | 0/0/0/0 | 左/中央 | 1.00 |
| P12 | text | Meiryo UI 12 | regular | #505050 | なし | なし | 0/0/0/0 | 右/中央 | 1.00 |
| PANEL | rect | なし | なし | なし | #F5F6F8 | #D0D5DD 1pt | — | なし | なし |
| WHITE | rect | なし | なし | なし | #FFFFFF | #D0D5DD 1pt | — | なし | なし |
| BLUE | rect | なし | なし | なし | #FFFFFF | #1F5FAF 2pt | — | なし | なし |
| BAR | rect | なし | なし | なし | #1F5FAF | なし | — | なし | なし |

| Line style | 幅 | 色 | head | z |
|---|---:|---|---|---:|
| FLOW | 2pt | #1F5FAF | target側に7pt三角 | 20 |
| REF | 1.5pt | #505050 | target側に6pt三角 | 20 |

## 06｜最初は、自分がAIの段取り係だった

**表示見出しはObject表の指定を使用。時間：45秒。**

制作メタ（非表示）：人が四工程を反復していた様子を示す。 口頭説明はslide-design.mdの第06枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| step1 | rect | PANEL | 40 | 200 | 205 | 130 |  | 10 |
| step2 | rect | PANEL | 265 | 200 | 205 | 130 |  | 10 |
| step3 | rect | PANEL | 490 | 200 | 205 | 130 |  | 10 |
| step4 | rect | PANEL | 715 | 200 | 205 | 130 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | 最初は自分が段取り係だった | 30 |
| intro | text | L20 | 40 | 111 | 880 | 36 | 一件の仕事を、人が毎回つないでいた | 30 |
| who1 | text | C20 | 56 | 165 | 173 | 25 | 自分 | 30 |
| step1Text | text | C22 | 54 | 224 | 177 | 80 | 事情を<br>説明 | 30 |
| who2 | text | C20 | 281 | 165 | 173 | 25 | 自分 | 30 |
| step2Text | text | C22 | 279 | 224 | 177 | 80 | 指示を<br>中継 | 30 |
| who3 | text | C20 | 506 | 165 | 173 | 25 | 自分 | 30 |
| step3Text | text | C22 | 504 | 224 | 177 | 80 | 結果を<br>読む | 30 |
| who4 | text | C20 | 731 | 165 | 173 | 25 | 自分 | 30 |
| step4Text | text | C22 | 729 | 224 | 177 | 80 | 止まれば<br>再開 | 30 |
| refrain | text | E24 | 40 | 440 | 880 | 35 | 段取りが、もう一つの仕事になった | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 06 / 13 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|
| step1To2 | step1:right@0.5 | step2:left@0.5 | なし | 1 | FLOW | 20 |
| step2To3 | step2:right@0.5 | step3:left@0.5 | なし | 1 | FLOW | 20 |
| step3To4 | step3:right@0.5 | step4:left@0.5 | なし | 1 | FLOW | 20 |
| repeat | step4:bottom@0.5 | step1:bottom@0.5 | (817.5,390); (142.5,390) | 3 | REF | 20 |

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|
| step1To2 | step1To2_s1 | (245,265) | (265,265) | 始点=step1:right@0.5 / 終点=step2:left@0.5 | FLOW | target側7pt三角 | 20 |
| step2To3 | step2To3_s1 | (470,265) | (490,265) | 始点=step2:right@0.5 / 終点=step3:left@0.5 | FLOW | target側7pt三角 | 20 |
| step3To4 | step3To4_s1 | (695,265) | (715,265) | 始点=step3:right@0.5 / 終点=step4:left@0.5 | FLOW | target側7pt三角 | 20 |
| repeat | repeat_s1 | (817.5,330) | (817.5,390) | 始点=step4:bottom@0.5 | REF | なし | 20 |
| repeat | repeat_s2 | (817.5,390) | (142.5,390) | 中継点 | REF | なし | 20 |
| repeat | repeat_s3 | (142.5,390) | (142.5,330) | 終点=step1:bottom@0.5 | REF | target側6pt三角 | 20 |
