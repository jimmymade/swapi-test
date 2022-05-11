# Test Suite for Star Wars API 

(https://swapi.dev/)


## Install locally with virtual env

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



