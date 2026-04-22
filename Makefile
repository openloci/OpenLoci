DOCS     = docs
PORT     = 1313
BASE_URL = https://openloci.org/

.DEFAULT_GOAL := help

.PHONY: docs docs-build check-uv install install-dev test clean uninstall help

check-uv: ## Verify uv is installed (required for all targets)
	@command -v uv >/dev/null 2>&1 || { \
		echo ""; \
		echo "  ✗  uv is not installed."; \
		echo "     Install it from: https://docs.astral.sh/uv/getting-started/installation/"; \
		echo "     Mac/Linux: curl -LsSf https://astral.sh/uv/install.sh | sh"; \
		echo "     Windows:   winget install --id=astral-sh.uv  (or see link above)"; \
		echo ""; \
		exit 1; \
	}
	@echo "  ✓  uv $$(uv --version)"

install: check-uv ## Install openloci CLI globally via uv tool  [run once after cloning]
	uv tool install --editable .

install-dev: check-uv ## Install dev dependencies for running tests and linting
	uv pip install -e ".[dev]"

docs: check-uv ## Spin up the OpenLoci docs site locally (http://localhost:$(PORT))
	cd "$(DOCS)" && hugo server --watch --port $(PORT)

docs-build: check-uv ## Build docs for deployment (sets baseURL to $(BASE_URL))
	cd "$(DOCS)" && hugo --minify --baseURL "$(BASE_URL)"

test: check-uv ## Run OpenLoci test suite
	uv run pytest tests/ -v

clean: ## Remove local build artifacts and caches (does NOT uninstall the global CLI)
	@echo "Removing local artifacts..."
	rm -rf .venv
	rm -rf src/openloci.egg-info
	rm -rf .pytest_cache
	rm -rf .ruff_cache
	rm -rf .mypy_cache
	rm -rf docs/public
	rm -rf docs/resources
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -name "*.pyc" -delete
	@echo "Done. To also remove the globally installed 'openloci' CLI, run: make uninstall"

uninstall: check-uv ## Remove the globally installed openloci CLI (installed by 'make install')
	uv tool uninstall openloci
	@echo "openloci CLI removed. Run 'make install' to reinstall."

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
