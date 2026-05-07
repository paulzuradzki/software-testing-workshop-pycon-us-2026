set shell := ["bash", "-uc"]

PORT := "8000"
PDF_PORT := "8765"
PDF_OUT := "slides.pdf"

# List available recipes
default:
    @just --list

# Serve slides at http://localhost:{{PORT}}
serve:
    @echo "→ http://localhost:{{PORT}}/"
    cd slides && python3 -m http.server {{PORT}}

# Alias for `serve`
dev: serve

# Render slides to {{PDF_OUT}} via decktape (needs Node.js / npx)
pdf:
    #!/usr/bin/env bash
    set -euo pipefail
    if ! command -v npx >/dev/null 2>&1; then
        echo "✗ npx not found. Install Node.js: https://nodejs.org/" >&2
        exit 1
    fi
    (cd slides && python3 -m http.server {{PDF_PORT}} >/tmp/slides-pdf-server.log 2>&1) &
    SERVER_PID=$!
    trap 'kill $SERVER_PID 2>/dev/null || true' EXIT
    for i in $(seq 1 20); do
        if curl -fsS "http://localhost:{{PDF_PORT}}/" >/dev/null 2>&1; then break; fi
        sleep 0.25
    done
    npx -y decktape@3 reveal "http://localhost:{{PDF_PORT}}/" "{{PDF_OUT}}"
    echo "✓ Wrote {{PDF_OUT}}"

# Remove generated PDF and Python caches
clean:
    rm -f {{PDF_OUT}}
    find . -type d \( -name __pycache__ -o -name .pytest_cache \) \
        -not -path './.venv/*' -not -path './.git/*' \
        -exec rm -rf {} +
    find . -type f -name '*.pyc' \
        -not -path './.venv/*' -not -path './.git/*' \
        -delete
