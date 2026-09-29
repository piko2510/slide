# 第09枚の制作仕様｜v6

出力：homelab_ai_09.pptx、1枚のみ。ページ番号：09 / 18。
同期元：talks/homelab-ai/slide-design.md、blob a1c1949f40559e04d2890862a74b4c6d944d68e0。
以下は対象ページの本文。話す内容はノートへ収録し、画面へ転載しない。

### 09｜中継を自分へ戻さないため、親が仕事を持つ

**時間：40秒**

**この一枚：** モデル名ではなく、本人の中継を減らすための担当と返却先を理解してもらう。

**掲載文言：**

> 親Astra：要求・割当・結果評価・最終受入
>
> Sol：通常の実働
> Luna：対象と到達点が明確な仕事
> Grok：コード実装（外部CLI）
>
> critic / verifier：別担当による確認
>
> 足りないと親が判断した時だけ、子Astraへ

**図・配置：** 親を上段、実働と確認を下段へまとめる。
指示と結果の戻りを分け、結果は本人でなく親へ返す線を強調する。
外部Grokはnative agentと同じ実装であるように描かない。
全モデルを毎回通す固定多段処理にしない。[^roles]

**話す内容：**

まず、結果の中継を私へ戻さないため、親、作業担当、確認担当に分けています。
親は依頼を整理して担当を選び、結果が戻っても、完了を判断するまで仕事を持ちます。
親がAstra、通常の作業がSolです。
対象と終了点が明確で結果を照合できる仕事はLuna、コード実装は外部CLIのGrokへ渡します。
必要な確認は別担当に頼み、その結果も親へ戻す。
全員を毎回通すのではなく、仕事に応じて選びます。

**台本外の技術注記：** 通常workerはSol/high、明確な仕事は既存workerへLuna/maxを指定する。
critic/verifierはSol/xhighのread-only role。
外部coderはworkerから限定CLIで起動し、Grok利用不能時の代替実装は親が同じ範囲・許可でSol/xhighへ明示割当する。
Lunaの汎用workerとread-onlyのcommit-workerを混同しない。
子Astraは親が担当の能力不足を判断した時の振り直し先であり、自動のエスカレーション階段ではない。
外部writer等の列挙やreasoning effortの説明は本編へ増やさない。

## 確認元（ノート用）

[^roles]: homelabの[担当契約](https://github.com/piko2510/homelab/blob/9485fc3c6e9fe61b076c45d48e55b6dc565bae0e/docs/ai-providers/vm133-provider-command-contract.md)。親・Sol・Luna・外部Grok・critic/verifier等の担当と権限。
