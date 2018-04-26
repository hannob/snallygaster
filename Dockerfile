FROM python:3-alpine

WORKDIR /app
ADD requirements.txt setup.py /app/
RUN pip install -r requirements.txt
RUN adduser -h /app -D app
USER app

ENV PATH "/app:$PATH"
ADD . /app/
