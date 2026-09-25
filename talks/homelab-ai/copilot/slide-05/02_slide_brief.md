# 第05枚 専用指示書
## 出力
- `homelab_ai_05.pptx`
- `05 / 13`
## 目的
独自Harnessを撤去し、**既存の標準機構へ責務を戻した**転換点を示す。
## 掲載文言
- タイトル：37万5900行消して、標準機能へ戻った
- 大きな数値：375,900 deletions
- 事実：300 files changed / 629 additions
- Before：独自Harnessが実行・状態・Gate・復旧を抱える
- After：
  - 実行ループ → Codex
  - 作業状態 → Git
  - Issue / PR / review / CI → GitHub
  - 自作 → 必要な接続部分
- 補足：GitHub差分上のdeletions。手書きLOCや性能改善率ではありません。
- 結論：薄くしたのは機能ではなく、「自分で持つ責任」。
## レイアウト
Before→大きな削減矢印→After。375,900を大きく見せるが、扇情的な赤や炎は禁止。補足は必ず残す。
