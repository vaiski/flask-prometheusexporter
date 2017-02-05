# -*- coding: utf-8 -*-

import time
import socket
from flask import request
from prometheus_client import start_http_server, Counter, Histogram

REQUEST_LATENCY = Histogram('flask_request_latency',
                            'Flask Request Latency in Seconds',
                            ['method', 'endpoint', 'hostname'])

REQUEST_COUNT = Counter('flask_request_count', 'Flask Request Count',
                        ['method', 'endpoint', 'http_status', 'hostname'])


def before_request():
    request.time = time.time()


def after_request_factory(hostname):
    def after_request(response):
        latency = time.time() - request.time
        REQUEST_LATENCY.labels(request.method, request.path, hostname).\
            observe(latency)
        REQUEST_COUNT.labels(request.method, request.path,
                             response.status_code, hostname).inc()
        return response
    return after_request


class Prometheus(object):

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self._port = app.config.get('PROMETHEUS_PORT', 9202)
        self._hostname = app.config.get('PROMETHEUS_HOSTNAME',
                                        socket.gethostname())
        self._setup_hooks(app)
        self._start()

    def _setup_hooks(self, app):
        app.before_request(before_request)
        app.after_request(after_request_factory(self._hostname))

    def _start(self):
        start_http_server(self._port)
