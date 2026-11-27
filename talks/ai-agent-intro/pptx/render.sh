#!/bin/sh
# 使い方：sh pptx/render.sh。LibreOffice（soffice）と pdftoppm が必要。
# Meiryo UI が無い環境では、呼ぶ側で FONTCONFIG_FILE を渡して代替フォントを指定できる。
set -eu

script_dir=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
talk_dir=$(CDPATH= cd -- "$script_dir/.." && pwd)
render_tmp=$(mktemp -d "${TMPDIR:-/tmp}/ai-agent-intro.XXXXXX")
trap 'rm -rf "$render_tmp"' 0
trap 'exit 1' HUP INT TERM
mkdir -p "$render_tmp/preview"

for deck in model skill; do
    soffice "-env:UserInstallation=file://$render_tmp/profile" \
        --headless --convert-to pdf --outdir "$render_tmp" \
        "$talk_dir/ai-agent-intro-$deck.pptx"
    test -s "$render_tmp/ai-agent-intro-$deck.pdf"
    pdftoppm -r 80 -png "$render_tmp/ai-agent-intro-$deck.pdf" \
        "$render_tmp/preview/$deck"
    for n in 1 2 3 4 5 6 7; do
        test -s "$render_tmp/preview/$deck-$n.png"
    done
done

mkdir -p "$talk_dir/preview"
for deck in model skill; do
    for n in 1 2 3 4 5 6 7; do
        padded=$(printf '%02d' "$n")
        mv "$render_tmp/preview/$deck-$n.png" "$talk_dir/preview/$deck-$padded.png"
    done
done
