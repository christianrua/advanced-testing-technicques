# advanced-testing-technicques
This is a repo for doing advance testing techniques

## Setup Project

1. Create and source virtual environment

```bash
python3 -m venv venv
venv source/bin/activate
```

2. Create scaffold

```bash
touch Makefile && touch test_hello.py && hello.py && requirements.txt
```

3. Populate the `Makefile`

```bash
install:
		pip install --upgrade && \
			pip install -r requirements.txt

test:
		python3 -m pytest -vv --cov=hello --cov=hellocli test_hello.py

lint:
		pylint --disable=R,C hello.py hellocli.pytest

all: install lint test
```

### How to debug

* Print
* pdb
* testing

