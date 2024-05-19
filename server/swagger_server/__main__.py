#!/usr/bin/env python3
import logging
from pprint import pprint

import connexion
from flask import request
from prometheus_client import Counter, Metric, Gauge, Summary, Histogram

from swagger_server import encoder

from prometheus_flask_exporter import PrometheusMetrics

from swagger_server.controllers import default_controller


logging.basicConfig(filename='E:/PyProects/oaslab/var/log/1.log', level=logging.INFO)


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    metrics = PrometheusMetrics(app.app)
    default_controller.books = []
    default_controller.authors = []



    d = Gauge('books', 'Number of books')
    d.set_function(lambda: len(default_controller.books))

    d1 = Gauge('authors', 'Number of authors')
    d1.set_function(lambda: len(default_controller.authors))


    '''metrics.register_default(
        metrics.counter(
            'custom_metric1', 'Request count by endpoints',
            labels={'endpoint': lambda: request.endpoint}
        )
    )'''

    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Хранение книг'}, pythonic_params=True)
    app.run(port=8080)


if __name__ == '__main__':
    main()
