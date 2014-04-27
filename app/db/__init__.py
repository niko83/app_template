# -*- coding: utf-8 -*-
from app import settings as app_settings
from app.db.postgresql.logic import get_connection as get_psql_connection
# from app.db.mysql.logic import get_connection as get_mysql_connection


def get_connection(db_key='default'):

    db_settings = app_settings.DB.get(db_key)
    if not db_settings:
        raise Exception('Not found db settings %s. Check app_settings.DB' % db_key)

    adapter = db_settings.get('ADAPTER', 'postgresql')
    if adapter == 'postgresql':
        return get_psql_connection(db_key)
    elif adapter == 'mysql':
        return get_mysql_connection(db_key)

    raise Exception('Unknown adapter %s' % adapter)

