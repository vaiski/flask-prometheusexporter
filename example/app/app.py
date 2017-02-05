# -*- coding: utf-8 -*-

import time
import random
from flask import Flask
from flask_prometheusexporter import Prometheus
from prometheus_client import Counter


app = Flask(__name__)
prom = Prometheus(app)

EX = Counter('flask_exceptions', 'Flask Exceptions')


@app.route('/')
def index():
    t = random.random()
    time.sleep(t)
    return "Hello World!"


@app.route('/error')
@EX.count_exceptions()
def error():
    return 1/0


if __name__ == '__main__':
    app.run(host='0.0.0.0')
