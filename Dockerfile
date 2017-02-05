FROM python:3.5-alpine

ADD . /app
WORKDIR /app
RUN pip install -e .[dev]

ENTRYPOINT ["python", "example/app/app.py"]
