FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

RUN /usr/local/bin/python -m pip install --upgrade pip && pip install -r requirements.txt

RUN rm /app/requirements.txt

CMD ["python", "main.py"]