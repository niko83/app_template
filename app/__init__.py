# -*- coding: utf-8 -*-
"""Base app settings, and settings witch should be replaced in settings_local.py file."""


class Settings(object):
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

settings = Settings()

execfile('/var/www/app_template/settings_local.py')

