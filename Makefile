PY = python3
FLAGS = --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
MAIN = a_maze_ing.py
CONFIG = config.txt

run:
	@$(PY) $(MAIN) $(CONFIG)

install:
	@pip install flake8
	@pip install mypy

debug:
	@$(PY) -m pdb $(MAIN) $(CONFIG)

clean:
	@rm -rf *__pycache__ */__pycache__
	@rm -rf .mypy_cache /.mypy_cache

lint:
	-flake8 .
	-mypy . $(FLAGS)
