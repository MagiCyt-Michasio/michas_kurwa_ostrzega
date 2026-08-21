#!/usr/bin/env bash
set -euo pipefail

source .venv/bin/activate
manim -qh "$1" "$2"
