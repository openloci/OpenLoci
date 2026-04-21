DOCS    = docs
PORT    = 1313
BASE_URL = https://openloci.org/

.DEFAULT_GOAL := help

.PHONY: docs docs-build install test help

docs: ## Spin up the OpenLoci docs site locally (http://localhost:$(PORT))
	cd "$(DOCS)" && hugo server --watch --port $(PORT)

docs-build: ## Build docs for deployment (sets baseURL to $(BASE_URL))
	cd "$(DOCS)" && hugo --minify --baseURL "$(BASE_URL)"

install: ## Install OpenLoci in dev mode (uv recommended)
	uv pip install -e ".[dev]"

test: ## Run OpenLoci test suite
	python -m pytest tests/ -v

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
