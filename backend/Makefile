# Makefile: Python virtual environment
# setup && activation

setup:
	# Create python virtualenv & source it
	# source venv/Scripts/activate ---GitBash
	python -m virtualenv venv

install:
	# this should be run from inside a virtualenv
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	# python test_flaskr.py

lint:
	# pylint: Linter for Python code view-source: https://www.pylint.org/
	# this should be run from inside a virtualenv
	pylint --disable=R,C,W1203,W1202 flaskr/__init__.py

all: install lint test
