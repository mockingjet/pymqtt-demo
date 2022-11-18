FROM python:3.9

RUN apt-get update
RUN apt-get -y upgrade
RUN pip install --upgrade pip
RUN pip install --no-cache-dir poetry 
RUN poetry config virtualenvs.create false