# 第11枚の制作仕様｜v6

出力：homelab_ai_11.pptx、1枚のみ。ページ番号：11 / 18。
同期元：talks/homelab-ai/slide-design.md、blob a1c1949f40559e04d2890862a74b4c6d944d68e0。
以下は対象ページの本文。話す内容はノートへ収録し、画面へ転載しない。

### 11｜毎回の作業手順を、Skillにまとめる

**時間：55秒**

**この一枚：** 共通規則に続け、毎回の手順説明を減らす方法として実在するSkillを紹介する。

**掲載文言：**

> 作成支援：$skill-creatorに、用途・発動条件・制約を渡す

左のフォルダは、実在する`.agents/skills/`配下の例。

```text
github-main-refresh/
├── SKILL.md
├── agents/
│   └── openai.yaml
└── scripts/
    └── refresh_main.py
```

右は「実物を発表用に短縮」と明記したSKILL.md。

```markdown
---
name: github-main-refresh
description: 作業前にmainを安全に最新化する。
---
## 手順
- originを確認してfetchする。
- cleanなmainを、ff可能時だけ更新。
- dirty・作業branchは変更しない。
## 禁止
- reset --hard、clean、force push
```

ファイルの横に短い役割ラベルを付ける。

> SKILL.md：選択の手掛かりと手順
> openai.yaml：表示名・説明・既定プロンプト
> refresh_main.py：状態判定と安全な更新

下部の結論：

> 手順はMarkdown。定型処理はPython。同じPythonをHookでも使う。

**図・配置：** 左のフォルダ構成と右のSKILL.mdを主役にする。
役割ラベルはファイルの近くに置き、別の大きな説明表を重ねない。
必要なら`.agents/skills/`はフォルダ図の上の共通パスとして分離し、パスを途中で不自然に折り返さない。
存在しないreferencesやassetsを、実物の構成として足さない。[^skill] [^refresh]

**話す内容：**

次に、毎回の作業手順を説明しなくてよいよう、仕事別にまとめるのがSkillです。
作成を助けるSkill Creatorには、用途、使う場面、禁止事項を伝えます。
実物の例は、mainを安全に最新化するgithub-main-refreshです。
フォルダには、手順のSKILL.md、表示情報のopenai.yaml、処理本体のPythonがあります。
nameとdescriptionが選択の手掛かりで、使う時に本文を読みます。
この例ではfetchし、変更のないmainをfast-forwardできる場合だけ更新します。
作業中の変更を消して、無理に合わせることはしません。
このPythonを、次のHookからも呼びます。

**台本外の技術注記：** Skill Creatorは作成支援であり、Skillの実行時に必ず通る仲介処理ではない。
この代表Skillを選ぶ理由は、エンジニアが用途を理解しやすく、次のHookと同じ処理本体を追えるため。
Skillの実物と追加・更新の履歴、validator通過の記録は確認したが、このSkillをCreatorで生成した当時の呼出しログは未確認。
そのため、上段は公式の作成方法、下段は実物の構造として説明し、生成ログ・生成時の会話を捏造しない。

SKILL.mdは必須で、補助スクリプトやagents/openai.yamlはこの例にある構成であり、すべてのSkillの必須ファイルではない。
実物はmerge・rebase等のGit操作中にはfetchもしない。
dirty、detached HEAD、作業branch、ahead、divergedではcheckoutを変更しない。
変更しないcheckoutで続けて編集する場合の隔離worktree作成はSkillの後続手順であり、refresh_main.py自体が自動作成するとは説明しない。
手動実行例は`python3 .agents/skills/github-main-refresh/scripts/refresh_main.py --cwd "$PWD"`。
結果のstatusとorigin_mainを確認してから編集へ進む。
PR #1263の過去の検証記録やPR #1389の手順修正は参考根拠であり、今回テストを再実行したという意味ではない。

## 確認元（ノート用）

[^skill]: OpenAI「[Build skills](https://developers.openai.com/codex/skills/)」。Skill Creator、name/description、必要時の本文読み込み、必須ファイルと任意の補助ファイル。
[^refresh]: homelabの[github-main-refresh](https://github.com/piko2510/homelab/tree/9485fc3c6e9fe61b076c45d48e55b6dc565bae0e/.agents/skills/github-main-refresh)にあるSKILL.md、agents/openai.yaml、scripts/refresh_main.py。[PR #1263](https://github.com/piko2510/homelab/pull/1263)は追加と過去の検証記録、[PR #1389](https://github.com/piko2510/homelab/pull/1389)は編集時だけworktreeへ進む手順の修正。
