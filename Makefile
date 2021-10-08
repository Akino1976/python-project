REPOSITORY := python-project
APP_ENVIRONMENT ?= test
CURRENT_DATE := $(shell echo `date +'%Y-%m-%d'`)
VERSION ?= $(CURRENT_DATE)
DOCKER_NETWORK = $(REPOSITORY)/$(VERSION)

export CURRENT_DATE
export VERSION
export REPOSITORY
export APP_ENVIRONMENT

COMPOSE_TEST_FLAGS := -f docker-compose-test.yaml
POETRY_FILE := poetry.lock pyproject.toml

tests/unit/%: %
	@echo "=> Moving $< to $@"
	@cp $< $@

tests/system/%: %
	@echo "=> Moving $< to $@"
	@cp $< $@


copy-unittests: $(patsubst %, tests/unit/%, $(POETRY_FILE))
copy-systemtests: $(patsubst %, tests/system/%, $(POETRY_FILE))

set-up-test-environment: copy-systemtests

unittests: copy-unittests
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm unittests

unittests-watch: copy-unittests
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm unittests-watch

systemtests: set-up-test-environment
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm systemtests

systemtests-watch: set-up-test-environment
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm systemtests-watch

tests: create-network unittests systemtests

build-%:
	docker-compose $(COMPOSE_TEST_FLAGS) build $*

run-%:
	docker-compose $(COMPOSE_TEST_FLAGS) run --rm $*

stop-containers:
	docker-compose $(COMPOSE_DEFAULT_FLAGS) kill

clear-containers: stop-containers
	docker-compose $(COMPOSE_DEFAULT_FLAGS) rm --force

stop-all-containers:
	docker ps -q | xargs -I@ docker stop @

clear-all-containers: stop-all-containers
	docker ps -aq | xargs -I@ docker rm @

clear-volumes: clear-all-containers
	docker volume ls -q | xargs -I@ docker volume rm @

clear-images: clear-volumes
	@echo "=>  Removing all containers"
	docker images -q | uniq | xargs -I@ docker rmi -f @

build-app:
	docker build \
		-t $(REPOSITORY)-$(APP_ENVIRONMENT):latest \
		-t $(REPOSITORY)-$(APP_ENVIRONMENT):$(VERSION) \
		.

run-application: build-app
	docker run --network=host -it  \
	$(REPOSITORY)-$(APP_ENVIRONMENT):$(VERSION) \
	run_jobs.py event-handler
