# -*- coding: utf-8 -*-
"""Base app settings, and settings witch should be replaced in settings_local.py file."""

DEBUG = True

AMQP = {
    'default': {
        'host': 'localhost',
        'virtual_host': '',
        'username': '',
        'password': '',
    }
}

DB_MYSQL = {
    'default': {
        'host': 'localhost',
        'name': '',
        'username': '',
        'password': '',
    }
}

DB_POSTGRESQL = {
    'default': {
        'host': 'localhost',
        'name': '',
        'username': '',
        'password': '',
    }
}
