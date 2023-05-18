#!/usr/bin/env bash
find . -name "*.pyc" -exec rm -rf {} \;
find . -name "*.py,cover" -exec rm -rf {} \;
find . -name "*.orig" -exec rm -rf {} \;
find . -name "__pycache__" -exec rm -rf {} \;
rm -rf build/
rm -rf dist/
rm -rf src/faker-file.egg-info/
rm -rf src/faker-file/var/
rm -rf .cache/
rm -rf .idea/
rm -rf htmlcov/
rm -rf .coverage
rm -rf .pytest_cache/
rm -rf .mypy_cache/
rm -rf .ruff_cache/
