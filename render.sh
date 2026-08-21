#!/usr/bin/env bash
set -euo pipefail
source .venv/bin/activate
manim -pqh "$1" "$2"
