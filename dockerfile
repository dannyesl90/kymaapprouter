FROM python:3.12-slim

COPY requirements.txt /requirements.txt

RUN pip install -r requirements.txt

WORKDIR /app

COPY . .

CMD [ "python","app.py" ]