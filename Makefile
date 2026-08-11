:PHONY: deps clean test

deps:
	uv sync

clean:
	find -type d -name "__pycache__" -exec rm -rf {} +

test:
	uv run pytest

build:
	docker build -t pwgen-cli:make_latest .

compile-requirements:
	uv pip compile pyproject.toml -o requirements.txt && uv pip compile pyproject.toml --group dev -o requirements_dev.txt