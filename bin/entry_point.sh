#!/bin/bash
set -euo pipefail

echo "Entry point script running"

CONFIG_FILE=_config.yml

start_jekyll() {
    # Never reset or remove the host's lockfile through the bind mount.
    if ! bundle check; then
        echo "Dependencies changed. Rebuild with docker compose up --build."
        exit 1
    fi
    bundle exec jekyll serve --watch --port=8080 --host=0.0.0.0 --livereload --verbose --trace --force_polling &
    jekyll_pid=$!
}

stop_jekyll() {
    if [ -n "${jekyll_pid:-}" ] && kill -0 "$jekyll_pid" 2>/dev/null; then
        kill "$jekyll_pid"
        wait "$jekyll_pid" || true
    fi
}

trap stop_jekyll EXIT
trap 'exit 0' INT TERM
start_jekyll

while true; do
    inotifywait -q -e modify,move,create,delete "$CONFIG_FILE"
    if [ $? -eq 0 ]; then
        echo "Change detected to $CONFIG_FILE, restarting Jekyll"
        stop_jekyll
        start_jekyll
    fi
done
