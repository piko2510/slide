# わしの家のAI環境：全13枚の制作仕様

副題：AIに任せたくて、作って、壊して、今こうなった

この文書は[発表設計](slide-design.md)の内容をPowerPointの1枚ごとの編集可能な図形へ写すための正本。表示見出しはoutlineの正式題名より短い場合がある。全表示文字は各Object表のText欄に限定する。口頭説明と制作メタ、style文書、object ID、座標、禁則の文章を画面へ載せない。接続線はConnector表にある論理経路をSegment表の直線本数で描き、それ以外は加えない。

計13枚、合計600秒。第04、09〜12枚は「公開スライドの旧生成セットを現行13枚へ揃えて公開する」同じ説明用の依頼を扱う。途中の判断と失敗は説明用に再構成しており、実行記録や観測済み障害ではない。第09枚の文脈取得は必要時の枝であり、この例に対応するContext DB記録の実在は仮定しない。第10枚のJevは参考資料だけの補助。指示・権限・受入条件は直通する。

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

## 01｜わしの家のAI環境

**表示見出しはObject表の指定を使用。時間：20秒。**

制作メタ（非表示）：主題と副題だけを大きく置き、本人の話として始める。 口頭説明はslide-design.mdの第01枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| cover | text | T40 | 60 | 153 | 840 | 60 | わしの家のAI環境 | 30 |
| subtitle | text | B24 | 60 | 225 | 840 | 45 | AIに任せたくて、作って、壊して、今こうなった | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 01 / 13 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|

## 02｜家に置いているものと、クラウドに任せるもの

**表示見出しはObject表の指定を使用。時間：60秒。**

制作メタ（非表示）：自宅VM、クラウド推論、GitHubの置き場所を一目で分ける。 口頭説明はslide-design.mdの第02枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| home | rect | PANEL | 170 | 138 | 430 | 292 |  | 10 |
| human | rect | WHITE | 40 | 245 | 100 | 80 |  | 10 |
| codex | rect | BLUE | 230 | 220 | 230 | 84 |  | 10 |
| db | rect | WHITE | 230 | 338 | 230 | 67 |  | 10 |
| cloud | rect | BLUE | 680 | 165 | 240 | 85 |  | 10 |
| github | rect | WHITE | 680 | 325 | 240 | 85 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | 家に置くものと、クラウド | 30 |
| homeLabel | text | L20 | 190 | 152 | 390 | 30 | 自宅：Proxmox上のVM | 30 |
| humanText | text | C20 | 50 | 269 | 80 | 32 | 人間 | 30 |
| codexText | text | C20 | 242 | 235 | 202 | 54 | Codex・tools<br>worktreeで作業 | 30 |
| dbText | text | C20 | 242 | 345 | 202 | 54 | Context DB<br>事情・理由・制約 | 30 |
| cloudText | text | C22 | 696 | 179 | 208 | 58 | クラウド<br>推論する先 | 30 |
| githubText | text | C20 | 696 | 339 | 208 | 58 | GitHub<br>要求・PR・公開状態 | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 02 / 13 | 40 |
| note | text | N14 | 40 | 470 | 790 | 25 | 自宅は作業と事情。モデル推論はクラウド。 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|
| humanToCodex | human:right@0.5 | codex:left@0.5 | (170,285); (170,262) | 3 | FLOW | 20 |
| codexToCloud | codex:right@0.35 | cloud:left@0.5 | (630,249.4); (630,207.5) | 3 | FLOW | 20 |
| codexToGithub | codex:right@0.75 | github:left@0.5 | (635,283); (635,367.5) | 3 | FLOW | 20 |
| dbToCodex | db:top@0.5 | codex:bottom@0.5 | なし | 1 | REF | 20 |

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|
| humanToCodex | humanToCodex_s1 | (140,285) | (170,285) | 始点=human:right@0.5 | FLOW | なし | 20 |
| humanToCodex | humanToCodex_s2 | (170,285) | (170,262) | 中継点 | FLOW | なし | 20 |
| humanToCodex | humanToCodex_s3 | (170,262) | (230,262) | 終点=codex:left@0.5 | FLOW | target側7pt三角 | 20 |
| codexToCloud | codexToCloud_s1 | (460,249.4) | (630,249.4) | 始点=codex:right@0.35 | FLOW | なし | 20 |
| codexToCloud | codexToCloud_s2 | (630,249.4) | (630,207.5) | 中継点 | FLOW | なし | 20 |
| codexToCloud | codexToCloud_s3 | (630,207.5) | (680,207.5) | 終点=cloud:left@0.5 | FLOW | target側7pt三角 | 20 |
| codexToGithub | codexToGithub_s1 | (460,283) | (635,283) | 始点=codex:right@0.75 | FLOW | なし | 20 |
| codexToGithub | codexToGithub_s2 | (635,283) | (635,367.5) | 中継点 | FLOW | なし | 20 |
| codexToGithub | codexToGithub_s3 | (635,367.5) | (680,367.5) | 終点=github:left@0.5 | FLOW | target側7pt三角 | 20 |
| dbToCodex | dbToCodex_s1 | (345,338) | (345,304) | 始点=db:top@0.5 / 終点=codex:bottom@0.5 | REF | target側6pt三角 | 20 |

## 03｜この環境でやりたい日常の仕事

**表示見出しはObject表の指定を使用。時間：40秒。**

制作メタ（非表示）：本人が減らしたい二つの負担を示す。 口頭説明はslide-design.mdの第03枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| goal1Bar | rect | BAR | 40 | 142 | 8 | 200 |  | 10 |
| goal2Bar | rect | BAR | 500 | 142 | 8 | 200 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | この環境でやりたいこと | 30 |
| goal1 | text | B28 | 64 | 170 | 390 | 112 | 一件の依頼を<br>公開確認まで任せたい | 30 |
| goal2 | text | B28 | 524 | 170 | 396 | 112 | 旧案と今の判断を<br>説明し直したくない | 30 |
| goalNote | text | B22 | 40 | 390 | 880 | 60 | 設計書だけ直して終わりにせず、生成入力と公開まで揃える | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 03 / 13 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|

## 04｜自分がAIに渡したい依頼

**表示見出しはObject表の指定を使用。時間：60秒。**

制作メタ（非表示）：旧生成セットを現行13枚に揃えて公開する説明例で、依頼の境界を見せる。 口頭説明はslide-design.mdの第04枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| request | rect | BLUE | 40 | 120 | 880 | 105 |  | 10 |
| card1 | rect | PANEL | 40 | 275 | 280 | 145 |  | 10 |
| card2 | rect | PANEL | 340 | 275 | 280 | 145 |  | 10 |
| card3 | rect | PANEL | 640 | 275 | 280 | 145 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | 自分がAIに渡したい依頼 | 30 |
| requestText | text | B28 | 66 | 135 | 828 | 75 | 古い公開スライド生成セットを<br>現行13枚の設計に揃えて公開して | 30 |
| card1Head | text | L20 | 58 | 290 | 244 | 30 | 目的 | 30 |
| card1Body | text | B22 | 58 | 330 | 244 | 72 | 13枚と生成入力を<br>同じ内容にする | 30 |
| card2Head | text | L20 | 358 | 290 | 244 | 30 | 範囲 | 30 |
| card2Body | text | B22 | 358 | 330 | 244 | 72 | 設計書と<br>各ページのbrief | 30 |
| card3Head | text | L20 | 658 | 290 | 244 | 30 | 終わり方 | 30 |
| card3Body | text | B22 | 658 | 330 | 244 | 72 | 公開mainを確認し<br>URLを返す | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 04 / 13 | 40 |
| exampleNote | text | N14 | 40 | 470 | 800 | 25 | 途中の判断と失敗は説明用に再構成。実行記録ではない。 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|

## 05｜自分に返ってきてほしいもの

**表示見出しはObject表の指定を使用。時間：60秒。**

制作メタ（非表示）：13枚、生成入力、公開確認という受取物と未確認を見せる。 口頭説明はslide-design.mdの第05枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| result1 | rect | BLUE | 40 | 160 | 280 | 150 |  | 10 |
| result2 | rect | BLUE | 340 | 160 | 280 | 150 |  | 10 |
| result3 | rect | BLUE | 640 | 160 | 280 | 150 |  | 10 |
| humanBand | rect | PANEL | 40 | 375 | 880 | 70 |  | 10 |
| humanBar | rect | BAR | 40 | 375 | 8 | 70 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | 自分に返ってきてほしいもの | 30 |
| resultIntro | text | L20 | 40 | 104 | 880 | 32 | 自分が受け取りたい結果 | 30 |
| result1Head | text | L20 | 58 | 181 | 244 | 30 | 更新したもの | 30 |
| result1Body | text | B22 | 58 | 224 | 244 | 70 | 13枚の設計と<br>生成用セット | 30 |
| result2Head | text | L20 | 358 | 181 | 244 | 30 | 確認した根拠 | 30 |
| result2Body | text | B22 | 358 | 224 | 244 | 70 | 題目・文言・条件の<br>整合結果 | 30 |
| result3Head | text | L20 | 658 | 181 | 244 | 30 | 公開と未確認 | 30 |
| result3Body | text | B22 | 658 | 224 | 244 | 70 | 公開URL<br>PPT実描画は未確認 | 30 |
| humanBandText | text | B22 | 65 | 391 | 832 | 40 | 新しい公開情報や外部共有は、自分が判断する | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 05 / 13 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|

## 06｜最初は、自分がAIの段取り係だった

**表示見出しはObject表の指定を使用。時間：45秒。**

制作メタ（非表示）：人が事情の説明、指示の中継、結果の確認、再開を反復していた様子を示す。 口頭説明はslide-design.mdの第06枚を参照し、画面へ転載しない。

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
| refrain | text | E24 | 40 | 440 | 880 | 35 | 任せるたび、説明・中継・再開が自分に戻る | 30 |
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

## 07｜事故を防ぐたびに、管理するものが増えた

**表示見出しはObject表の指定を使用。時間：45秒。**

制作メタ（非表示）：二重実行や古いheadへの対策と、独自状態を照合する負担を対応させる。 口頭説明はslide-design.mdの第07枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| row1 | rect | PANEL | 40 | 150 | 880 | 60 |  | 10 |
| row2 | rect | PANEL | 40 | 217 | 880 | 60 |  | 10 |
| row3 | rect | PANEL | 40 | 284 | 880 | 60 |  | 10 |
| row4 | rect | PANEL | 40 | 351 | 880 | 60 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | 事故を防ぐほど管理が増えた | 30 |
| accidentHead | text | L20 | 58 | 105 | 390 | 35 | 防ぎたかった事故 | 30 |
| mechanismHead | text | L20 | 535 | 105 | 385 | 35 | 足した仕組み | 30 |
| row1Left | text | B22 | 58 | 163 | 435 | 34 | 二重実行 | 30 |
| row1Right | text | B22 | 535 | 163 | 365 | 34 | claim / lease | 30 |
| row2Left | text | B22 | 58 | 230 | 435 | 34 | 古いheadで公開する | 30 |
| row2Right | text | B22 | 535 | 230 | 365 | 34 | 対象headの照合 | 30 |
| row3Left | text | B22 | 58 | 297 | 435 | 34 | 中断後の再開点が不明 | 30 |
| row3Right | text | B22 | 535 | 297 | 365 | 34 | checkpoint / receipt | 30 |
| row4Left | text | B22 | 58 | 364 | 435 | 34 | 許可範囲を越える | 30 |
| row4Right | text | B22 | 535 | 364 | 365 | 34 | Authority / gate | 30 |
| result | text | E24 | 40 | 450 | 880 | 40 | GitHubと独自状態を突き合わせる仕事が増えた | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 07 / 13 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|

## 08｜独自Harnessを撤去して、標準機能へ戻した

**表示見出しはObject表の指定を使用。時間：45秒。**

制作メタ（非表示）：撤去と責務の移管先、規則と強いモデルへの集中という残る癖を示す。 口頭説明はslide-design.mdの第08枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| old | rect | PANEL | 40 | 160 | 245 | 230 |  | 10 |
| standard | rect | BLUE | 420 | 160 | 500 | 230 |  | 10 |
| remaining | rect | PANEL | 40 | 402 | 880 | 54 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | 独自Harnessを撤去した | 30 |
| metric | text | E24 | 40 | 102 | 880 | 38 | 375,900 deletions | 30 |
| oldHead | text | B28 | 56 | 192 | 213 | 76 | 独自<br>Harness | 30 |
| oldBody | text | B22 | 56 | 292 | 213 | 70 | claim・復旧点も<br>自前で管理 | 30 |
| standardHead | text | L20 | 438 | 180 | 464 | 30 | 標準機能へ戻した責任 | 30 |
| standardRow1 | text | B22 | 438 | 224 | 464 | 30 | Codex：実行 | 30 |
| standardRow2 | text | B22 | 438 | 258 | 464 | 30 | Git：変更 | 30 |
| standardRow3 | text | B22 | 438 | 292 | 464 | 30 | GitHub：開発状態 | 30 |
| standardRow4 | text | B22 | 438 | 326 | 464 | 30 | 自作：接続・入力加工・安全境界 | 30 |
| remainingText | text | B22 | 58 | 410 | 844 | 36 | 規則が太ると、強いモデルへ調査・完了条件が集中 | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 08 / 13 | 40 |
| metricNote | text | N14 | 40 | 470 | 820 | 25 | 撤去commit差分：300 files changed / 629 additions。手書きLOC・効果の値ではない。 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|
| transfer | old:right@0.5 | standard:left@0.5 | なし | 1 | FLOW | 20 |

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|
| transfer | transfer_s1 | (285,275) | (420,275) | 始点=old:right@0.5 / 終点=standard:left@0.5 | FLOW | target側7pt三角 | 20 |

## 09｜作り直した今のハーネスの全体像

**表示見出しはObject表の指定を使用。時間：45秒。**

制作メタ（非表示）：同じ説明用依頼の具体入力と戻り値を三大段階で見る。この例に対応するContext DB記録の実在は仮定しない。 口頭説明はslide-design.mdの第09枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| stage1 | rect | BLUE | 40 | 150 | 270 | 210 |  | 10 |
| stage2 | rect | BLUE | 345 | 150 | 270 | 210 |  | 10 |
| stage3 | rect | BLUE | 650 | 150 | 270 | 210 |  | 10 |
| context | rect | WHITE | 95 | 400 | 160 | 50 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | 今のハーネスの全体像 | 30 |
| example | text | L20 | 40 | 98 | 880 | 32 | 説明用：旧生成セットを現行13枚へ揃えて公開 | 30 |
| stage1Head | text | L20 | 58 | 172 | 234 | 30 | 入力を整える | 30 |
| stage1Body | text | B22 | 58 | 225 | 234 | 84 | 親Astraが範囲確認<br>旧案と現行を分ける<br>事情を必要時に取得 | 30 |
| stage2Head | text | L20 | 363 | 172 | 234 | 30 | 担当が実行 | 30 |
| stage2Body | text | B22 | 363 | 225 | 234 | 84 | 13枚とbriefを同期<br>差分を照合 | 30 |
| stage3Head | text | L20 | 668 | 172 | 234 | 30 | 根拠で受入 | 30 |
| stage3Body | text | B22 | 668 | 225 | 234 | 84 | 親が公開mainを確認<br>URLと未確認を返す | 30 |
| contextText | text | C20 | 105 | 410 | 140 | 30 | Context DB | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 09 / 13 | 40 |
| condition | text | N14 | 320 | 469 | 500 | 27 | 事情は必要時に参照。過去の記録は現在の許可ではない。 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|
| stage1To2 | stage1:right@0.5 | stage2:left@0.5 | なし | 1 | FLOW | 20 |
| stage2To3 | stage2:right@0.5 | stage3:left@0.5 | なし | 1 | FLOW | 20 |
| contextUp | context:top@0.5 | stage1:bottom@0.5 | なし | 1 | REF | 20 |

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|
| stage1To2 | stage1To2_s1 | (310,255) | (345,255) | 始点=stage1:right@0.5 / 終点=stage2:left@0.5 | FLOW | target側7pt三角 | 20 |
| stage2To3 | stage2To3_s1 | (615,255) | (650,255) | 始点=stage2:right@0.5 / 終点=stage3:left@0.5 | FLOW | target側7pt三角 | 20 |
| contextUp | contextUp_s1 | (175,400) | (175,360) | 始点=context:top@0.5 / 終点=stage1:bottom@0.5 | REF | target側6pt三角 | 20 |

## 10｜担当に、何を渡すか

**表示見出しはObject表の指定を使用。時間：40秒。**

制作メタ（非表示）：現行13枚の必須条件と、旧案を含む参考資料を別レーンから渡す。 口頭説明はslide-design.mdの第10枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| required | rect | BLUE | 40 | 150 | 305 | 130 |  | 10 |
| reference | rect | PANEL | 40 | 295 | 305 | 100 |  | 10 |
| jev | rect | WHITE | 385 | 295 | 205 | 100 |  | 10 |
| recipient | rect | BLUE | 680 | 150 | 240 | 260 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | 担当に何を渡すか | 30 |
| requiredHead | text | L20 | 55 | 163 | 275 | 30 | 現在の必須情報 | 30 |
| requiredBody | text | B22 | 55 | 198 | 275 | 78 | 現行13枚・起承転結<br>10分・3添付・1枚生成<br>白・Meiryo UI・編集可 | 30 |
| referenceHead | text | L20 | 55 | 305 | 275 | 28 | Context DBの参考情報 | 30 |
| referenceBody | text | B22 | 55 | 336 | 275 | 56 | 過去の判断理由<br>時点・出典・訂正 | 30 |
| jevHead | text | L20 | 398 | 304 | 180 | 28 | 限定選別 | 30 |
| jevBody | text | B22 | 398 | 334 | 180 | 56 | 旧案を候補化<br>Jevが関係判定 | 30 |
| recipientHead | text | L20 | 696 | 178 | 208 | 30 | 担当への入力 | 30 |
| recipientBody | text | B22 | 696 | 235 | 208 | 100 | 現在の13枚と<br>維持する生成条件<br>必要な事情だけ | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 10 / 13 | 40 |
| note | text | N14 | 40 | 470 | 790 | 25 | 必須条件は直通。不確実な参考資料は落とさない。 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|
| requiredDirect | required:right@0.5 | recipient:left@0.25 | なし | 1 | FLOW | 20 |
| referenceToJev | reference:right@0.5 | jev:left@0.5 | なし | 1 | REF | 20 |
| jevToRecipient | jev:right@0.5 | recipient:left@0.75 | なし | 1 | REF | 20 |

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|
| requiredDirect | requiredDirect_s1 | (345,215) | (680,215) | 始点=required:right@0.5 / 終点=recipient:left@0.25 | FLOW | target側7pt三角 | 20 |
| referenceToJev | referenceToJev_s1 | (345,345) | (385,345) | 始点=reference:right@0.5 / 終点=jev:left@0.5 | REF | target側6pt三角 | 20 |
| jevToRecipient | jevToRecipient_s1 | (590,345) | (680,345) | 始点=jev:right@0.5 / 終点=recipient:left@0.75 | REF | target側6pt三角 | 20 |

## 11｜任せた担当が、どこまで進めるか

**表示見出しはObject表の指定を使用。時間：40秒。**

制作メタ（非表示）：briefに旧題名が残る説明用の局所失敗で、担当の修正と戻す境界を示す。 口頭説明はslide-design.mdの第11枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| work1 | rect | BLUE | 40 | 160 | 250 | 180 |  | 10 |
| work2 | rect | BLUE | 355 | 160 | 250 | 180 |  | 10 |
| work3 | rect | BLUE | 670 | 160 | 250 | 180 |  | 10 |
| boundary | rect | PANEL | 40 | 412 | 880 | 44 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | 担当はどこまで進めるか | 30 |
| exampleFailure | text | B22 | 40 | 96 | 880 | 35 | 更新漏れ：生成指示に旧題名が残る | 30 |
| exampleNote | text | N14 | 40 | 134 | 880 | 20 | 説明用に再構成した局所失敗。実行記録ではない。 | 30 |
| work1Head | text | L20 | 56 | 182 | 218 | 30 | 調べる | 30 |
| work1Body | text | B22 | 56 | 236 | 218 | 70 | 設計書とbriefの<br>題名を照合 | 30 |
| work2Head | text | L20 | 371 | 182 | 218 | 30 | 修正する | 30 |
| work2Body | text | B22 | 371 | 236 | 218 | 70 | 同じ担当が<br>旧題名を更新 | 30 |
| work3Head | text | L20 | 686 | 182 | 218 | 30 | 検証する | 30 |
| work3Body | text | B22 | 686 | 236 | 218 | 70 | 13枚の題目を<br>もう一度確認 | 30 |
| boundaryText | text | B22 | 58 | 417 | 844 | 34 | 新しい公開情報や外部共有は親へ返し、本人が判断 | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 11 / 13 | 40 |
| roles | text | N14 | 40 | 471 | 810 | 23 | 配役：Solは通常実働、Lunaは照合、コード実装ならGrok。 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|
| work1To2 | work1:right@0.5 | work2:left@0.5 | なし | 1 | FLOW | 20 |
| work2To3 | work2:right@0.5 | work3:left@0.5 | なし | 1 | FLOW | 20 |
| recheck | work3:bottom@0.5 | work2:bottom@0.5 | (795,390); (480,390) | 3 | REF | 20 |

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|
| work1To2 | work1To2_s1 | (290,250) | (355,250) | 始点=work1:right@0.5 / 終点=work2:left@0.5 | FLOW | target側7pt三角 | 20 |
| work2To3 | work2To3_s1 | (605,250) | (670,250) | 始点=work2:right@0.5 / 終点=work3:left@0.5 | FLOW | target側7pt三角 | 20 |
| recheck | recheck_s1 | (795,340) | (795,390) | 始点=work3:bottom@0.5 | REF | なし | 20 |
| recheck | recheck_s2 | (795,390) | (480,390) | 中継点 | REF | なし | 20 |
| recheck | recheck_s3 | (480,390) | (480,340) | 終点=work2:bottom@0.5 | REF | target側6pt三角 | 20 |

## 12｜何を見て、終わったと判断するか

**表示見出しはObject表の指定を使用。時間：40秒。**

制作メタ（非表示）：13枚とbrief、公開main、未描画という結果と到達点を親が照合する。 口頭説明はslide-design.mdの第12枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| result | rect | PANEL | 40 | 165 | 250 | 125 |  | 10 |
| parent | rect | BLUE | 355 | 175 | 250 | 105 |  | 10 |
| target | rect | PANEL | 670 | 165 | 250 | 125 |  | 10 |
| git | rect | WHITE | 105 | 355 | 270 | 75 |  | 10 |
| github | rect | WHITE | 585 | 355 | 270 | 75 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | 何を見て終わったと判断するか | 30 |
| resultHead | text | L20 | 56 | 181 | 218 | 28 | 結果と根拠 | 30 |
| resultBody | text | B22 | 56 | 220 | 218 | 62 | 13枚とbrief<br>URL・PPT未描画 | 30 |
| parentHead | text | L20 | 373 | 190 | 214 | 30 | 親Astraが照合 | 30 |
| parentBody | text | B22 | 373 | 227 | 214 | 40 | 到達点と根拠 | 30 |
| targetHead | text | L20 | 686 | 181 | 218 | 28 | 依頼の到達点 | 30 |
| targetBody | text | B22 | 686 | 220 | 218 | 62 | 題目・文言一致<br>必須条件の保持 | 30 |
| gitHead | text | L20 | 121 | 365 | 238 | 25 | Git | 30 |
| gitBody | text | B22 | 121 | 397 | 238 | 27 | 変更・差分・main | 30 |
| githubHead | text | L20 | 601 | 365 | 238 | 25 | GitHub | 30 |
| githubBody | text | B22 | 601 | 397 | 238 | 27 | PR・merge・公開URL | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 12 / 13 | 40 |
| note | text | N14 | 40 | 470 | 790 | 25 | 公開済みとPPT実描画は別。新しい公開情報は本人判断。 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|
| resultToParent | result:right@0.5 | parent:left@0.5 | なし | 1 | FLOW | 20 |
| targetToParent | target:left@0.5 | parent:right@0.5 | なし | 1 | FLOW | 20 |
| gitToParent | git:top@0.5 | parent:bottom@0.3 | (240,320); (430,320) | 3 | REF | 20 |
| githubToParent | github:top@0.5 | parent:bottom@0.7 | (720,320); (530,320) | 3 | REF | 20 |

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|
| resultToParent | resultToParent_s1 | (290,227.5) | (355,227.5) | 始点=result:right@0.5 / 終点=parent:left@0.5 | FLOW | target側7pt三角 | 20 |
| targetToParent | targetToParent_s1 | (670,227.5) | (605,227.5) | 始点=target:left@0.5 / 終点=parent:right@0.5 | FLOW | target側7pt三角 | 20 |
| gitToParent | gitToParent_s1 | (240,355) | (240,320) | 始点=git:top@0.5 | REF | なし | 20 |
| gitToParent | gitToParent_s2 | (240,320) | (430,320) | 中継点 | REF | なし | 20 |
| gitToParent | gitToParent_s3 | (430,320) | (430,280) | 終点=parent:bottom@0.3 | REF | target側6pt三角 | 20 |
| githubToParent | githubToParent_s1 | (720,355) | (720,320) | 始点=github:top@0.5 | REF | なし | 20 |
| githubToParent | githubToParent_s2 | (720,320) | (530,320) | 中継点 | REF | なし | 20 |
| githubToParent | githubToParent_s3 | (530,320) | (530,280) | 終点=parent:bottom@0.7 | REF | target側6pt三角 | 20 |

## 13｜今の自宅AI環境で目指していること

**表示見出しはObject表の指定を使用。時間：60秒。**

制作メタ（非表示）：冒頭の環境図と目的に戻り、課題を残す。 口頭説明はslide-design.mdの第13枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| human | rect | WHITE | 40 | 250 | 85 | 70 |  | 10 |
| home | rect | PANEL | 150 | 145 | 255 | 260 |  | 10 |
| codex | rect | BLUE | 180 | 210 | 215 | 65 |  | 10 |
| db | rect | WHITE | 180 | 312 | 215 | 65 |  | 10 |
| cloud | rect | BLUE | 450 | 170 | 125 | 82 |  | 10 |
| github | rect | WHITE | 450 | 300 | 125 | 82 |  | 10 |
| issues | rect | PANEL | 620 | 145 | 300 | 260 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | 今の環境で目指すこと | 30 |
| humanText | text | C20 | 48 | 268 | 69 | 34 | 人間 | 30 |
| homeLabel | text | L20 | 163 | 159 | 228 | 28 | 自宅のVM | 30 |
| codexText | text | C20 | 190 | 229 | 195 | 28 | Codex・作業場 | 30 |
| dbText | text | C20 | 190 | 331 | 195 | 28 | Context DB・事情 | 30 |
| cloudText | text | C20 | 461 | 186 | 103 | 50 | クラウド<br>推論 | 30 |
| githubText | text | C20 | 461 | 321 | 103 | 34 | GitHub | 30 |
| issuesHead | text | L20 | 640 | 169 | 260 | 30 | まだ調整中 | 30 |
| issuesBody | text | B22 | 640 | 220 | 260 | 105 | 規則の保守<br>文脈の選び方<br>担当の配役 | 30 |
| closing | text | E24 | 40 | 445 | 880 | 48 | 公開確認まで任せ、説明・中継・再開を減らす | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 13 / 13 | 40 |
| measurement | text | N14 | 640 | 365 | 260 | 24 | Jev全体効果：未測定 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|
| humanToCodex | human:right@0.5 | codex:left@0.5 | (140,285); (140,242.5) | 3 | FLOW | 20 |
| dbToCodex | db:top@0.5 | codex:bottom@0.5 | なし | 1 | REF | 20 |
| codexToCloud | codex:right@0.35 | cloud:left@0.5 | (425,232.75); (425,211) | 3 | FLOW | 20 |
| codexToGithub | codex:right@0.75 | github:left@0.5 | (430,258.75); (430,341) | 3 | FLOW | 20 |

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|
| humanToCodex | humanToCodex_s1 | (125,285) | (140,285) | 始点=human:right@0.5 | FLOW | なし | 20 |
| humanToCodex | humanToCodex_s2 | (140,285) | (140,242.5) | 中継点 | FLOW | なし | 20 |
| humanToCodex | humanToCodex_s3 | (140,242.5) | (180,242.5) | 終点=codex:left@0.5 | FLOW | target側7pt三角 | 20 |
| dbToCodex | dbToCodex_s1 | (287.5,312) | (287.5,275) | 始点=db:top@0.5 / 終点=codex:bottom@0.5 | REF | target側6pt三角 | 20 |
| codexToCloud | codexToCloud_s1 | (395,232.75) | (425,232.75) | 始点=codex:right@0.35 | FLOW | なし | 20 |
| codexToCloud | codexToCloud_s2 | (425,232.75) | (425,211) | 中継点 | FLOW | なし | 20 |
| codexToCloud | codexToCloud_s3 | (425,211) | (450,211) | 終点=cloud:left@0.5 | FLOW | target側7pt三角 | 20 |
| codexToGithub | codexToGithub_s1 | (395,258.75) | (430,258.75) | 始点=codex:right@0.75 | FLOW | なし | 20 |
| codexToGithub | codexToGithub_s2 | (430,258.75) | (430,341) | 中継点 | FLOW | なし | 20 |
| codexToGithub | codexToGithub_s3 | (430,341) | (450,341) | 終点=github:left@0.5 | FLOW | target側7pt三角 | 20 |
