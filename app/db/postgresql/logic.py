# -*- coding: utf-8 -*-
import psycopg2
import psycopg2.extras
from app import settings as app_settings

_connection_collection = {}


class _Cursor(psycopg2.extras.DictCursor):
    def execute(self, *args, **kwargs):
        return super(_Cursor, self).execute(*args, **kwargs)


def get_connection(db_key='default'):
    global _connection_collection

    if db_key in _connection_collection and not _connection_collection[db_key].closed:
        return _connection_collection[db_key]

    db_settings = app_settings.DB.get(db_key)
    connect = psycopg2.connect(
        database=db_settings['NAME'],
        user=db_settings['USER'],
        password=db_settings['PASSWORD'],
        host=db_settings['HOST'],
        port=db_settings['PORT'],
        cursor_factory=_Cursor,
    )
    connect.autocommit = True
    _connection_collection[db_key] = connect
    return connect
