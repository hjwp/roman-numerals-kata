.venv:
	python3.12 -m venv .venv

.PHONY: system-deps
system-deps:
	which watchexec || brew install watchexec

.PHONY: install
install: system-deps .venv pyproject.toml
	pip install .


.PHONY: commit
commit:
	git add .
	git commit -m "generic commit msg"
	git push

.PHONY: test
test:
	pytest tests.py

.PHONY: watch-tests
watch-tests:
	watchexec $(MAKE) test
