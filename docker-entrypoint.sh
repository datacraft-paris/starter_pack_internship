#!/bin/sh
set -e
ls /app
exec uv run python -m docker.main
