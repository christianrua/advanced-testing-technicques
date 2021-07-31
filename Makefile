install:
		pip install --upgrade && pip install -r requirements.txt

test:
		python3 -m pytest -vv --cov=hello --cov=hellocli test_hello.py

lint:
		pylint --disable=R,C hello.py hellocli.pytest

all: install lint test