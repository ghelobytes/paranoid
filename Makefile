help: ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nTargets:\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2 }' $(MAKEFILE_LIST)

install: ## Install dependencies
	poetry install

code-check: ## Apply code checks to source code
	clear
	@echo 
	@echo "Running isort ..."
	isort -rc .

	@echo 
	@echo "Running black ..."
	black . --exclude "/app/migrations/versions/"

	@echo 
	@echo "Running flake ..."
	flake8 . --exclude=.*

	@echo
	@echo "Running safety check ..."
	safety check 

test: ## Run tests
	clear
	poetry run pytest tests --verbose --maxfail=1 -s
