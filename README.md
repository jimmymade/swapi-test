# Test Suite for Star Wars API 

Test suite to test the Star Wars public API (https://swapi.dev/).

## Install locally with virtual env
Steps to setup your virtual environment and run tests

1. Setup virtual env:

  ```sh
  python3 -m venv .venv
  source .venv/bin/activate
  python -m pip install --upgrade pip
  pip install -r requirements.txt
  ```

2. Run Tests

  ```sh
  pytest -vvs --capture=tee-sys
  ```

## Run with Docker
Steps to build and run docker image with tests. You will need to have docker installed and running

1. Build image

  ```sh
  docker build . -t swapi-test:latest
  ```

2. Run image

  ```sh
  docker run swapi-test:latest
  ```

