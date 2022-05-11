# Test Suite for Star Wars API 

Test suite to test the Star Wars public API (https://swapi.dev/).

Contains api tests written in python leverging the pytest libary to run tests. 
Tests are currently just leveraging the public api and making validation based on assumptions after reading the documentation. There are limitations to the tests that can be created due to not having direct access to the database the api is pulling from.

Documentation also specifies a rate limiting system. It would be ideal to be able to test this, but be able to deploy and configure the rate limit of the api to a separate non production environment. This way we would be able to test the rate limiting feature but at a much smaller scale. 

Also, at the time or writing it looks the like the /schema feature of the api is not working properly. For example making the request to  https://swapi.dev/api/<resource>/schema returns a 404. The test written for this has been commented out. It would have been nice to be able to fetch the JSON schema and leverage it for better typing.
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

