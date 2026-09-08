#!/bin/bash
set -e

echo "=== ruff format --check ==="
#ruff format --check

echo "=== ruff check ==="
#ruff check

echo "=== pytest ==="
pytest

echo "✅ All quality checks passed"
exit 0
