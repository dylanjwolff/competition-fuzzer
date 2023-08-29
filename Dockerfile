FROM python:slim

RUN apt update -y
RUN apt install -y git pkg-config libcairo-dev gcc

RUN useradd student

WORKDIR /home/student

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY *.py ./
COPY examples ./examples

ENTRYPOINT /bin/bash
