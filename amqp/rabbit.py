# -*- coding: utf-8 -*-
"""RabbitMQ functions."""

import pika
import settings

_connection = {}


def get_connection(name='default'):
    """get amqp connection by name."""
    connect = _connection.get(name)
    if connect and not connect.close and not connect.closing:
        return connect

    conn_settings = settings.AMQP[name]
    connect = pika.ConnectionParameters(
        host=conn_settings['host'],
        virtual_host=conn_settings['virtual_host'],
        credentials=pika.credentials.PlainCredentials(
            conn_settings['username'],
            conn_settings['password'],
        ),
    )

    _connection[name] = connect
    return connect
