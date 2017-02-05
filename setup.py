# -*- coding: utf-8 -*-
"""
Flask-PrometheusExporter
------------------------

Adds Prometheus monitoring support to your Flask application.
"""

from setuptools import setup

VERSION = '0.1.0'

setup(
    name='Flask-PrometheusExporter',
    version=VERSION,
    url='http://github.com/vaiski/flask-prometheusexporter',
    license='MIT',
    author=u'Eemil Väisänen',
    author_email='eemil.vaisanen@iki.fi',
    description='Adds Prometheus monitoring support to your Flask application',
    long_description=__doc__,
    packages=['flask_prometheusexporter'],
    install_requires=[
        'prometheus_client',
    ],
    extras_require={
        'dev': [
            'Flask',
        ],
        'test': [
            'pytest',
            'pytest-cov',
            'pylint',
            'flake8'
        ]
    },
    test_suite='tests',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Framework :: Flask',
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ]
)
