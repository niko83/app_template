# -*- coding: utf-8 -*-
"""Base app settings, and settings witch should be replaced in settings_local.py file."""
import os


class Settings(object):
    DEBUG = True

    AMQP = {
        'default': {
            'HOST': 'localhost',
            'VIRTUAL_HOST': '',
            'USER': '',
            'PASSWORD': '',
        }
    }

    DB = {
        'default': {
            'ADAPTER': 'postgresql',
            'HOST': 'localhost',
            'PORT': 5432,
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
        },
        'second_db': {
            'ADAPTER': 'mysql',
            'HOST': 'localhost',
            'PORT': 3306,
            'NAME': '',
            'USER': '',
            'PASSWORD': '',
        }
    }

    INCLUDED_PATCH_FOR_SEARCH_COMMANDS = ('app.commands', 'app.migrations.commands')
    MIGRATIONS = (
        'app.migrations.0001_init_migrations_table.Migration',
    )

    PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__).decode('utf-8') + '/../') + os.sep

settings = Settings()

execfile(settings.PROJECT_ROOT + '/settings_local.py')
