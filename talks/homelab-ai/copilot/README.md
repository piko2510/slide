# Copilotで1枚ずつ生成するセット

**各スライドのフォルダに「貼り付けるプロンプト1つ＋添付するテキスト3つ」を揃えています。**
対象はCopilot Chat Basicでの1枚ずつの生成です。
完成したPowerPointではなく、生成を依頼するための入力一式です。
更新日：2026-09-24。

## 使い方

1. 下の一覧から対象スライドを開き、`00_style_guide.txt`、`01_talk_outline.txt`、`02_slide_brief.txt`の3ファイルを端末へ保存します。
2. Copilotで対象の1枚用の新しいチャットを開き、この3ファイルだけを添付します。
3. 同じフォルダの`prompt.txt`の中身をチャット欄に貼って送信します。**`prompt.txt`は添付しません。**

受け取るファイル名は`homelab_ai_01.pptx`〜`homelab_ai_13.pptx`です。
各ファイルに入るスライドは1枚だけです。
最初は[第1枚](slide-01/)で見た目を確認し、残りも同じ手順で生成します。
既存スライドや追加の画像を添付する必要はありません。

## 1枚分のフォルダの中身

```text
slide-01/
├── prompt.txt             ← 本文をチャット欄へ貼る。添付しない
├── 00_style_guide.txt     ← 添付1：白背景・Meiryo UIなど
├── 01_talk_outline.txt    ← 添付2：全体の文脈。全13枚の生成指示ではない
└── 02_slide_brief.txt     ← 添付3：この1枚の確定文言・図・配置
```

`00_style_guide.txt`と`01_talk_outline.txt`は全13フォルダで同じ内容です。
別の場所から探して組み合わせなくても、そのスライドのフォルダだけで3添付が揃います。
各専用指示書には、掲載する文言、図の箱と接続、配置、載せない内容、確認点を記載しています。
テキストはUTF-8です。

## スライド別リンク

各リンク先のファイル画面から内容を表示・保存できます。
フォルダ名のリンクは、その1枚に必要な4ファイルの一覧です。

| 枚・テーマ | 貼り付け用 | 添付1 | 添付2 | 添付3 |
| --- | --- | --- | --- | --- |
| [01 自宅AI環境の裏側](slide-01/) | [プロンプト](slide-01/prompt.txt) | [デザイン](slide-01/00_style_guide.txt) | [全体文脈](slide-01/01_talk_outline.txt) | [専用指示](slide-01/02_slide_brief.txt) |
| [02 AIを使うための仕事を減らしたい](slide-02/) | [プロンプト](slide-02/prompt.txt) | [デザイン](slide-02/00_style_guide.txt) | [全体文脈](slide-02/01_talk_outline.txt) | [専用指示](slide-02/02_slide_brief.txt) |
| [03 自宅の作業場とクラウド](slide-03/) | [プロンプト](slide-03/prompt.txt) | [デザイン](slide-03/00_style_guide.txt) | [全体文脈](slide-03/01_talk_outline.txt) | [専用指示](slide-03/02_slide_brief.txt) |
| [04 依頼が結果になるまで](slide-04/) | [プロンプト](slide-04/prompt.txt) | [デザイン](slide-04/00_style_guide.txt) | [全体文脈](slide-04/01_talk_outline.txt) | [専用指示](slide-04/02_slide_brief.txt) |
| [05 GitHubで要求と現在地を確かめる](slide-05/) | [プロンプト](slide-05/prompt.txt) | [デザイン](slide-05/00_style_guide.txt) | [全体文脈](slide-05/01_talk_outline.txt) | [専用指示](slide-05/02_slide_brief.txt) |
| [06 ルール・手順・機械処理を分ける](slide-06/) | [プロンプト](slide-06/prompt.txt) | [デザイン](slide-06/00_style_guide.txt) | [全体文脈](slide-06/01_talk_outline.txt) | [専用指示](slide-06/02_slide_brief.txt) |
| [07 コンテキスト基盤](slide-07/) | [プロンプト](slide-07/prompt.txt) | [デザイン](slide-07/00_style_guide.txt) | [全体文脈](slide-07/01_talk_outline.txt) | [専用指示](slide-07/02_slide_brief.txt) |
| [08 Jevの情報選別](slide-08/) | [プロンプト](slide-08/prompt.txt) | [デザイン](slide-08/00_style_guide.txt) | [全体文脈](slide-08/01_talk_outline.txt) | [専用指示](slide-08/02_slide_brief.txt) |
| [09 判断と実行の担当](slide-09/) | [プロンプト](slide-09/prompt.txt) | [デザイン](slide-09/00_style_guide.txt) | [全体文脈](slide-09/01_talk_outline.txt) | [専用指示](slide-09/02_slide_brief.txt) |
| [10 三つの起動方法](slide-10/) | [プロンプト](slide-10/prompt.txt) | [デザイン](slide-10/00_style_guide.txt) | [全体文脈](slide-10/01_talk_outline.txt) | [専用指示](slide-10/02_slide_brief.txt) |
| [11 進める・戻す・終える](slide-11/) | [プロンプト](slide-11/prompt.txt) | [デザイン](slide-11/00_style_guide.txt) | [全体文脈](slide-11/01_talk_outline.txt) | [専用指示](slide-11/02_slide_brief.txt) |
| [12 実装と効果は別](slide-12/) | [プロンプト](slide-12/prompt.txt) | [デザイン](slide-12/00_style_guide.txt) | [全体文脈](slide-12/01_talk_outline.txt) | [専用指示](slide-12/02_slide_brief.txt) |
| [13 流れは単純に、責任は明確に](slide-13/) | [プロンプト](slide-13/prompt.txt) | [デザイン](slide-13/00_style_guide.txt) | [全体文脈](slide-13/01_talk_outline.txt) | [専用指示](slide-13/02_slide_brief.txt) |

## 全ページの共通条件

白背景、16:9、日本語・英数字ともMeiryo UI、濃いグレーの文字、青1色の強調です。
タイトル32pt、本文・図中の主要説明22〜24ptを基本とし、読めないほどの縮小を避けます。
図はPowerPointの編集可能な図形・テキスト・コネクタで作り、画像貼り付けにしないよう指定しています。
追加表紙・空白ページ・発表者ノートは作らない指定です。
各回に追加添付を要求せず、前の生成結果にも依存しない入力にしています。

## 内容上の注意

Jevの図では、必須指示・権限・受入条件を選別の対象にせず、参考資料とは別経路で保持します。
モデルの配役を固定の自動昇格ルートとして描きません。
実装・限定的な動作確認・仕事全体の効果を区別し、未測定の効果を実績として補わせません。
内部設定・実メール・個人情報・非公開リポジトリの内容を添付する必要はありません。
内容の正本は[公開用の構成案](../outline.md)です。このセットはその具体化であり、元の構成案を削除・置換していません。

## 確認範囲

このセットに完成版の.pptxは含まれません。
Copilot Chat Basic上での実際の生成、表示、ダウンロード、フォント描画はこのリポジトリ登録時点では未確認です。
利用環境で生成できない場合に、ファイルや実績を捏造せず制約を明示する指示も含めています。
Meiryo UIのフォントファイルは含めていません。生成後の実ファイルで指定・表示・編集可能性を確認してください。
