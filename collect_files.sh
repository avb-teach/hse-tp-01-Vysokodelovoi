#!/usr/bin/env bash
if [[ "$3" == "--max_depth" ]]; then
  MAX_DEPTH="$4"
  INPUT_DIR="$1"
  OUTPUT_DIR="$2"
else
  MAX_DEPTH="-1"
  INPUT_DIR="$1"
  OUTPUT_DIR="$2"
fi

echo $MAX_DEPTH $INPUT_DIR $OUTPUT_DIR | python3 script.py
