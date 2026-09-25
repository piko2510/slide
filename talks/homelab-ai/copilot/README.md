# わしの家のAI環境：Copilot 1枚生成セット

現行の[全13枚の制作仕様](../production-spec.md)を、Copilot 5.6 Think（極高）で1枚ずつPowerPointへ転記するための入力一式です。自動生成の成功や実レンダリング結果は保証しません。

対象のslide-01〜slide-13で次の3ファイルを添付し、同じフォルダのprompt.md本文をチャット欄へ貼り付けます。prompt.mdは添付しません。

1. 00_style_guide.md（共通の寸法、style、接続線の規則）
2. 01_talk_outline.md（発表の順序。画面へ転載しない）
3. 02_slide_brief.md（当該1枚の全objectとconnector。表示文字の正本）

各ページは1枚だけ、homelab_ai_NN.pptxとして返す指定です。02_slide_brief.mdだけでも該当ページのstyleと座標が揃う構成にしています。見切れや描画未確認はpromptの条件どおり報告してください。
