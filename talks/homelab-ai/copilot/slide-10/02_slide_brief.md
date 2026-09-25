# 第10枚の制作仕様

出力：homelab_ai_10.pptx、1枚のみ、40秒のページ。
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

## 10｜担当に、何を渡すか

**表示見出しはObject表の指定を使用。時間：40秒。**

制作メタ（非表示）：必須情報と参考資料を別レーンから同じ入力へ合流させる。 口頭説明はslide-design.mdの第10枚を参照し、画面へ転載しない。

### Object表

| ID | 種別 | Style | x | y | w | h | Text（表示文字） | z |
|---|---|---|---:|---:|---:|---:|---|---:|
| required | rect | BLUE | 40 | 150 | 260 | 130 |  | 10 |
| reference | rect | PANEL | 40 | 295 | 260 | 100 |  | 10 |
| jev | rect | WHITE | 385 | 295 | 205 | 100 |  | 10 |
| recipient | rect | BLUE | 680 | 150 | 240 | 260 |  | 10 |
| title | text | T32 | 40 | 28 | 880 | 48 | 担当に何を渡すか | 30 |
| requiredHead | text | L20 | 55 | 163 | 230 | 30 | 現在の必須情報 | 30 |
| requiredBody | text | B22 | 55 | 198 | 230 | 78 | 目的・範囲<br>必須指示・権限<br>受入条件 | 30 |
| referenceHead | text | L20 | 55 | 305 | 230 | 28 | 参考資料 | 30 |
| referenceBody | text | B22 | 55 | 338 | 230 | 50 | Context DBの事情 | 30 |
| jevHead | text | L20 | 398 | 304 | 180 | 28 | 限定選別 | 30 |
| jevBody | text | B22 | 398 | 334 | 180 | 56 | コード候補化<br>Jevで関係判定 | 30 |
| recipientHead | text | L20 | 696 | 178 | 208 | 30 | 担当への入力 | 30 |
| recipientBody | text | B22 | 696 | 235 | 208 | 100 | 現在の依頼と<br>必要な事情<br>コードで組立 | 30 |
| page | text | P12 | 860 | 498 | 60 | 14 | 10 / 13 | 40 |
| note | text | N14 | 40 | 470 | 790 | 25 | 説明用。Jevは参考資料の補助。全体効果は未測定。 | 40 |

### Connector表（論理経路）

| 論理ID | source | target | waypoints（pt） | segment数 | Style | z |
|---|---|---|---|---:|---|---:|
| requiredDirect | required:right@0.5 | recipient:left@0.25 | なし | 1 | FLOW | 20 |
| referenceToJev | reference:right@0.5 | jev:left@0.5 | なし | 1 | REF | 20 |
| jevToRecipient | jev:right@0.5 | recipient:left@0.75 | なし | 1 | REF | 20 |

### Segment表（描画座標）

| 論理ID | segment ID | 始点(x,y) | 終点(x,y) | 境界固定 | Style | head | z |
|---|---|---|---|---|---|---|---:|
| requiredDirect | requiredDirect_s1 | (300,215) | (680,215) | 始点=required:right@0.5 / 終点=recipient:left@0.25 | FLOW | target側7pt三角 | 20 |
| referenceToJev | referenceToJev_s1 | (300,345) | (385,345) | 始点=reference:right@0.5 / 終点=jev:left@0.5 | REF | target側6pt三角 | 20 |
| jevToRecipient | jevToRecipient_s1 | (590,345) | (680,345) | 始点=jev:right@0.5 / 終点=recipient:left@0.75 | REF | target側6pt三角 | 20 |
