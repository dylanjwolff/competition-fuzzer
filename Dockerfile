FROM python:3.10-slim-bookworm

RUN apt update -y
RUN apt install -y git pkg-config libcairo-dev gcc

RUN useradd student

WORKDIR /home/student

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
# Don't change anything above here please!

# Add any additional files or dependencies needed for
# your fuzzer below here!
# -------------------------------------------

# For example, to add new Python packages:
# RUN pip install numpy

# For example, to add new files:
# COPY mynewfile.json ./

COPY *.py ./
COPY examples ./examples

ENTRYPOINT /bin/bash
