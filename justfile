set shell := ["bash", "-uc"]

# List available recipes
default:
    @just --list

# Remove pytest cache and __pycache__ folders
clean:
    find . -type d \( -name __pycache__ -o -name .pytest_cache \) \
        -not -path './.venv/*' -not -path './.git/*' \
        -exec rm -rf {} +
    find . -type f -name '*.pyc' \
        -not -path './.venv/*' -not -path './.git/*' \
        -delete
