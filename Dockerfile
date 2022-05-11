FROM python:3.8.5-slim-buster

# Copy and install requirements first to cache results
# and reduce build time on subsequent builds with code changes
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

COPY . /app
WORKDIR /app

CMD ["bash", "-c", "python -m pytest -vvs --capture=tee-sys"]