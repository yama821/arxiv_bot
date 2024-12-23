FROM python:3.11-slim

# update the certificates
# RUN apk update && apk add ca-certificates && update-ca-certificates

# install packages
COPY pyproject.toml poetry.lock ./
RUN pip install poetry
RUN poetry install
