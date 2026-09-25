# わしの家のAI環境：制作仕様 v3

副題：AIに任せたくて、作って、壊して、今こうなった

この制作仕様は、後半で現在のCodexハーネスを説明する版の正本である。

## 方針

- 独自Harnessの開発過程は、前半で「肥大化したので捨てた」と説明して終える。
- 後半は、現在の`homelab`で動かしているCodexハーネスの構造を説明する。
- 現在のハーネスは、独自runtimeではなく、Codex標準agent、AGENTS.md、Git、GitHub、systemd timer、Context DB、Jev前処理を薄く接続するものとして扱う。
- Jevは親・監督・最終判断役ではない。コードでは決めにくい意味関係を選ぶ限定前処理である。
- すべてのスライドは編集可能なPowerPoint図形で作る。写真、ロゴ、画像化した一枚絵へ逃げない。

## 共通style

| 項目 | 指定 |
|---|---|
| 画面 | 16:9、13.333 × 7.5 inch |
| 背景 | 白 `#FFFFFF` |
| フォント | Meiryo UI |
| 本文色 | `#222222` |
| 補足色 | `#505050` |
| 主色 | 青 `#1F5FAF` |
| 危険色 | 赤 `#B42318` |
| 補助面 | `#F5F6F8` |
| 枠線 | `#D0D5DD` |
| 見出し | 30〜34pt bold |
| 本文 | 19〜26pt |
| 注記 | 12〜14pt |
| ページ番号 | 右下に `NN / 13` |

## スライド一覧

| # | 表示見出し | 主メッセージ | 画面構成 |
|---:|---|---|---|
| 01 | わしの家のAI環境 | 作って、壊して、現在の設計へ至った話 | タイトルのみ大きく置く |
| 02 | 何をAIに任せたかったか | 一件の依頼を到達点まで任せたい | 左に依頼文、右に到達点の縦フロー |
| 03 | 任せたはずなのに自分が忙しい | 説明・中継・確認・再開が人間へ戻る | 人間を中心に四つの負担が戻るループ |
| 04 | 事故を防ぐほど仕組みが増えた | 正しい対策が独自状態を増やした | 事故と対策の二列対応 |
| 05 | 独自Harnessを捨てた | 375,900 deletionsを転換点として見せる | 大きな数字と、標準へ戻す矢印 |
| 06 | ここからは今のCodexハーネス | 過去話を閉じて現在形へ切り替える | 左に「捨てたもの」、右に「残したもの」 |
| 07 | 今の全体像 | Codex標準agentを中心に薄く接続する | Owner、Astra、AGENTS、agent、Git/GitHub、Context/Jev、timer |
| 08 | 状態管理は自作しない | 状態の正本はGitとGitHubへ戻す | 状態の種類と正本の対応表 |
| 09 | 親Astraと実働サブ | 判断と実行の責務を分ける | 親Astraを上に置き、Sol/Luna/Grok/leafへ分岐 |
| 10 | AGENTS.mdは境界線 | 実行機ではなく責務と戻し条件の定義 | AGENTS.mdを中央に置き、五つの問いを周囲に置く |
| 11 | Context DBとJevは入力側 | 必要な事情だけ受け手に渡す | Context→候補生成→Jev→assembler→workerの流れ |
| 12 | Issueからmergeまで | 実際のライフサイクルを示す | Issue/直接依頼からpost-merge verificationまでの横フロー |
| 13 | 作るのは接着剤まで | もう一つの状態機械を作らない | 結論文を大きく置き、薄い接着層を下に置く |

## 各スライドの表示文字

### 01

- わしの家のAI環境
- AIに任せたくて、作って、壊して、今こうなった

### 02

- 「これ直しておいて」で、調査・修正・確認・報告まで進んでほしい
- 人間は毎回、事情説明と再開係をやりたくない
- 調査
- 修正
- 検証
- 報告

### 03

- 事情を説明する
- 指示を中継する
- 結果を読む
- 止まれば再開する
- AIに任せたはずなのに、俺が一番忙しい

### 04

- 二重実行 → claim / lease
- 古いhead → head照合
- 再開不能 → checkpoint / receipt
- 権限逸脱 → gate / authority
- 正しい対策を足すほど、自分で管理する状態が増えた

### 05

- 375,900 deletions
- 独自Harnessを撤去し、標準へ戻した
- 状態管理はGitとGitHubへ戻す
- Codex標準agentを使う
- 300 files changed / 629 additions。効果測定値ではない。

### 06

- Harnessをなくしたわけではない
- Harnessの責務を標準機能へ戻した
- 捨てた：独自状態機械
- 残した：AGENTS.md / Git / GitHub / Codex標準agent / systemd timer

### 07

- Owner / Issue
- 親Astra
- AGENTS.md
- Codex標準agent
- Git / GitHub
- Context DB / Jev
- systemd timer
- 独自runtimeではなく、薄い接続

### 08

- 作業状態 → Git
- 要求 → GitHub Issue
- 変更 → branch / commit / diff
- 確認 → PR / review / CI
- 完了 → merge + post-merge verification
- 同じ状態を独自ledgerやreceiptへ複製しない

### 09

- 親Astra：要求・設計・安全境界・受入・merge判断
- Sol/high：通常worker
- Luna/max：対象が明確な定型作業
- Grok：コード実装
- critic / verifier：read-only確認
- 子Astra：Solで足りない時だけ振り直し

### 10

- 誰が判断するか
- 誰に渡すか
- どこまで進めるか
- どこで親へ返すか
- 何を完了とするか
- 実行基盤を自作せず、Codex標準agentへ責務を渡す

### 11

- Context DB：事情・理由・制約・訂正を必要時に引く
- コード：候補を作る
- Jev：意味関係だけ選ぶ
- assembler：受け手へ渡す本文を組む
- 必須指示・権限・受入条件はJevで選別しない

### 12

- Issue / 直接依頼
- 親Astraがscopeと受入条件を決める
- Context / Jevで入力を整える
- workerが隔離worktreeで実行
- test / review
- 親Astraが受入
- merge
- post-merge verification

### 13

- 作るのは接着剤まで
- もう一つの状態機械は作らない
- Codex標準、Git、GitHub、AGENTS.md、Context/Jevを薄くつなぐ
- 未完成でも、増やす前に「作らない」を見る

## スピーカーノート方針

- 01〜05は、汗と血を感じる導入にする。
- ただし、過去の枝葉の失敗談を長くしない。
- 06で明確に現在のハーネス説明へ切り替える。
- 07〜12では、実際の`homelab`の責務分離と運用を説明する。
- 13では、完成宣言ではなく設計思想として締める。
