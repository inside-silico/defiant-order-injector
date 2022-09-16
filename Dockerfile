# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster
RUN apt update
RUN apt install git -y

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN pip3 install git+https://github.com/franco-lamas/PyOBD --upgrade --no-cache-dir

COPY . .

CMD [ "python3","-u", "app.py"]
