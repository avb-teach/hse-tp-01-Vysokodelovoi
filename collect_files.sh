if [[ "$1" == "--max_depth" ]]; then
  MAX_DEPTH="$2"
  INPUT_DIR="$3"
  OUTPUT_DIR="$4"
else
  MAX_DEPTH="-1"
  INPUT_DIR="$1"
  OUTPUT_DIR="$2"
fi

echo $MAX_DEPTH $INPUT_DIR $OUTPUT_DIR | python3 script.py
