# Variables
APP_NAME=app
ROOT=$(shell pwd)

## Lint
DOCKER_IMAGE_LINTER=alvarofpp/linter:latest
LINT_COMMIT_TARGET_BRANCH=origin/main

# Commands
.PHONY: install-hooks
install-hooks:
	git config core.hooksPath .githooks

.PHONY: build
build: install-hooks
	@docker compose build --pull

.PHONY: build-no-cache
build-no-cache: install-hooks
	@docker compose build --no-cache --pull

.PHONY:
down:
	@docker compose down

.PHONY:
up:
	@docker compose up ${SERVICE_NAME}

.PHONY:
up-silent:
	@docker compose up -d ${SERVICE_NAME}

.PHONY: lint
lint:
	@docker pull ${DOCKER_IMAGE_LINTER}
	@docker run --rm -v ${ROOT}:/app ${DOCKER_IMAGE_LINTER} " \
		lint-commit ${LINT_COMMIT_TARGET_BRANCH} \
		&& lint-markdown \
		&& lint-dockerfile \
		&& lint-yaml \
		&& lint-shell-script \
		&& lint-python"

.PHONY: lint-fix
lint-fix:
	@docker pull ${DOCKER_IMAGE_LINTER}
	@docker run --rm -v ${ROOT}:/app ${DOCKER_IMAGE_LINTER} " \
		lint-python-fix"

.PHONY: shell
shell:
	@docker compose run --rm ${APP_NAME} bash
