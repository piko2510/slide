# 第12枚の制作仕様｜v6

出力：homelab_ai_12.pptx、1枚のみ。ページ番号：12 / 18。
同期元：talks/homelab-ai/slide-design.md、blob a1c1949f40559e04d2890862a74b4c6d944d68e0。
以下は対象ページの本文。話す内容はノートへ収録し、画面へ転載しない。

### 12｜呼ぶタイミングも、Hookに任せる

**時間：45秒**

**この一枚：** 手順が存在することと、必要な場面で呼ばれることを分け、イベントから同じ処理を呼ぶ経路を示す。

**掲載文言：**

左は`.codex/hooks.json`の起動時部分の説明用短縮例。
「commandは短縮表示・実行用設定ではない」と明記する。

```json
{
  "hooks": {
    "SessionStart": [{
      "matcher": "^startup$",
      "hooks": [{"type": "command",
        "command": "…refresh_main.py",
        "timeout": 20}]
    }]
  }
}
```

右は、このリポジトリに定義されている二つの呼出し経路。

```text
SessionStart / startup
  → refresh_main.py
  → Git確認・fetch・安全条件で更新

PreToolUse / Agent
  → jev_preprocess_agent.py
  → assemble-recipient.mjs
  → 対象の入力を差し替え
```

下部の結論：

> 呼出しはイベントから。有効化・信頼確認が前提。
> 資料の前処理は、対象外・失敗時には元の入力を通す。

**図・配置：** 左に短い設定、右に上下二つの処理の流れ。
SessionStartから11と同じPythonへつながることを強調する。
Jev側は入口だけを示し、候補選択の詳細は16へ送る。
JSON全文、全パス、SHA-256文字列、全例外分岐を画面へ詰め込まない。[^hooks]

**話す内容：**

でも、手順を置くだけでは、必要な場面で必ず使われるとは限りません。
そこで、決まったイベントから処理を呼ぶHookを使います。
画面のSessionStartは起動時で、先ほどのPythonを直接呼ぶ定義です。
Skillをモデルが選ぶ経路とは別です。
別のAIへ資料を渡す直前の前処理にも、Hookの定義があります。
ただし、有効化と信頼確認が前提で、資料の前処理は対象外や失敗時に元の入力を通します。
置けば必ず効く、ではなく、実際に通ったかも確認が必要です。

**台本外の技術注記：** 確認対象はリポジトリの`.codex/hooks.json`であり、ユーザー層・システム層を含む実機全体のHook一覧ではない。
設定のmatcherはSessionStartが`^startup$`、PreToolUseが`^Agent$`。
実際のcommandはGitルートを求め、スクリプトのSHA-256を照合してからPythonを実行する。
初回・定義変更後には`/hooks`でproject layerと現在の定義をreview・trustする必要があり、現在の実機で有効・信頼済みかはこの資料更新では未確認。

呼出先の実パスは、起動時が`.agents/skills/github-main-refresh/scripts/refresh_main.py`、入力前処理が`.codex/hooks/jev_preprocess_agent.py`、その先が`scripts/jev/assemble-recipient.mjs`。
SessionStart側はstdinのイベント情報からcwdを使い、status等をadditionalContextで返す。
手動実行では11の`--cwd`を用いる。
Git状態に関する指示の返却と、実行を機械的に停止できることを同一視しない。

Jev側スクリプトはAgent/spawn_agentを受け付けるが、設定上のmatcherと対応する実行経路の確認は別である。
対象はJSONとして読め、family・purpose・required・supplementaryのいずれかを持つ構造化入力。
無効化、対象外入力、assembler不在・失敗・timeout等では入力の差し替えを返さず、元の入力を通す設計である。
これは前処理を強制する安全境界ではなく、失敗時も元入力を保持する入力書換えHook。
資料取得後や親への全入力を、このHook一本ですべて前処理できるとは説明しない。
実APIの利用可否、実際の通過率、受け手での利用は17の別の確認事項とする。

## 確認元（ノート用）

[^hooks]: homelabの[.codex/hooks.json](https://github.com/piko2510/homelab/blob/9485fc3c6e9fe61b076c45d48e55b6dc565bae0e/.codex/hooks.json)、[jev_preprocess_agent.py](https://github.com/piko2510/homelab/blob/9485fc3c6e9fe61b076c45d48e55b6dc565bae0e/.codex/hooks/jev_preprocess_agent.py)、[refresh_main.py](https://github.com/piko2510/homelab/blob/9485fc3c6e9fe61b076c45d48e55b6dc565bae0e/.agents/skills/github-main-refresh/scripts/refresh_main.py)と、OpenAI「[Hooks](https://developers.openai.com/codex/hooks/)」。イベント、matcher、直接実行、信頼確認、構造化入力の差し替えと失敗時の扱い。
