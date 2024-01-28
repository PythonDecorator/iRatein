FROM python:3.9

ENV PYTHONUNBUFFERED 1

COPY requirements.txt /server/requirements.txt

RUN pip install -r /app/requirements.txt

COPY ./server /server
WORKDIR /server
EXPOSE 8000

