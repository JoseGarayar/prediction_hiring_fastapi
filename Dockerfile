FROM python:3.12.2

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

CMD [ "python3", "app.py" ]