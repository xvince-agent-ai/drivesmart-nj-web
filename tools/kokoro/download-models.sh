#!/usr/bin/env bash
set -euo pipefail
DIR="$(cd "$(dirname "$0")" && pwd)/models"
mkdir -p "$DIR"
BASE="https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0"
if [[ ! -f "$DIR/kokoro-v1.0.onnx" ]]; then
  curl -L --fail -o "$DIR/kokoro-v1.0.onnx" "$BASE/kokoro-v1.0.onnx"
fi
if [[ ! -f "$DIR/voices-v1.0.bin" ]]; then
  curl -L --fail -o "$DIR/voices-v1.0.bin" "$BASE/voices-v1.0.bin"
fi
echo "Models ready in $DIR"
