# {{cookiecutter.palace_name}} — OpenLoci palace
# make          → spins up the journal at http://localhost:1337
# make help     → print this

JOURNAL = The Vestibule/Journal
PORT    = 1337

.DEFAULT_GOAL := journal

.PHONY: journal journal-build new-post help

journal: ## Spin up the palace journal (http://localhost:$(PORT))
	cd "$(JOURNAL)" && hugo server --watch --port $(PORT)

journal-build: ## Build journal static files to The Vestibule/Journal/public/
	cd "$(JOURNAL)" && hugo --minify

new-post: ## Create a new session post — usage: make new-post TITLE="My Session"
	cd "$(JOURNAL)" && hugo new "posts/$$(date +%Y-%m-%d-%H%M)-$$(echo '$(TITLE)' | tr '[:upper:]' '[:lower:]' | tr ' ' '-').md"

help: ## Show available commands
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
