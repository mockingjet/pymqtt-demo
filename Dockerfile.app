FROM python:3.9

RUN apt-get update \
    && apt-get -y upgrade \
    && pip install --upgrade pip \
    && pip install --no-cache-dir poetry \ 
    && poetry config virtualenvs.create false

WORKDIR /app

COPY poetry.lock pyproject.toml /app

RUN poetry install --no-interaction --no-ansi