# advanced-testing-technicques
This is a repo for doing advance testing techniques

AWS CODE BUILD
https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoiS3dQeUhyc1kvYkNvRUE0S0ptcnJuWE1GNlFGRzRleWdndE9RQnBQNmdHOE5ZcFRHMUFJTzM2dGxiQ0ZCeFBqVnoyR0x3ZkxhdmEyREllQnZKc1JlTW9FPSIsIml2UGFyYW1ldGVyU3BlYyI6IklsSWhkaWZJZ1RHL0pqakUiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main

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

