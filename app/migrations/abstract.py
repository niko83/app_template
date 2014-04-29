#-*- coding: utf-8 -*-
import os
from app import settings as app_settings
from app.db import get_connection


class _COLORS(object):
    reset = "\x1b[0m"
    red = "\x1b[31;01m"
    green = "\x1b[32;01m"
    yellow = "\x1b[33;01m"
    white = "\x1b[37;01m"


def color(text, color_code=_COLORS.green):
    return ''.join([color_code, text, _COLORS.reset])


_SQL_MIGRATION_TABLE = """
    CREATE TABLE IF NOT EXISTS migrations (
        id smallserial,
        migration_key char(32),
        created_at timestamp without time zone default now(),
        UNIQUE(migration_key)
    )
"""


class AbstractMigration(object):

    MIGRATION_KEY = None
    DB_KEY = 'default'

    @property
    def conn(self):
        return get_connection(self.DB_KEY)

    def apply_raw_sql_file(self, sql_file_path):
        full_path = app_settings.PROJECT_ROOT + sql_file_path
        if not os.path.isfile(full_path):
            raise Exception('File %s does not exists' % full_path)

        with open(full_path, 'r') as f:
            self.execute_sql(f.read())
            print '  Execute raw_sql file: %s' % full_path

    def execute_sql(self, sql_commands):
        print '  SQL command is: \n%s' % sql_commands
        cursor = self.conn.cursor()

        try:
            cursor.execute('BEGIN')
            cursor.execute(sql_commands)
            cursor.execute('COMMIT')
        except:
            cursor.execute('ROLLBACK')
            print '  ' + color('ERROR', _COLORS.red)
            raise
        else:
            self._mark_migration_as_executed()

        self.conn.commit()
        print '  ' + color('OK')

    def _is_migration_executed(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT 1 from pg_tables WHERE tablename=%s', ('migrations', ))
        if not cursor.rowcount:
            cursor.execute(_SQL_MIGRATION_TABLE)
            print 'Migrations table success initialized.'
            print '-' * 50

        cursor.execute('SELECT * FROM migrations WHERE migration_key=%s', (
            self.MIGRATION_KEY,
        ))
        if cursor.rowcount:
            print '  Migration %s was executed %s.' % (
                color(self.MIGRATION_KEY, _COLORS.white),
                cursor.fetchone()['created_at'],
            )
            return True
        return False

    def _mark_migration_as_executed(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO migrations (migration_key) values (%s)', (
            self.MIGRATION_KEY,
        ))
        cursor.close()

    @staticmethod
    def logger(*args):
        if len(args) > 1:
            print args[0] % args[1:]
        else:
            print args[0]

    def run(self):

        if not self.MIGRATION_KEY:
            AbstractMigration.logger(
                'Migration %s is wrong.', color(self.__class__, _COLORS.white)
            )
            raise Exception('MIGRATION_KEY is not defined. Check your migration class')

        if not self._is_migration_executed():
            AbstractMigration.logger(
                'Run migration %s.', color(self.MIGRATION_KEY, _COLORS.white),
            )
            self._execute_migration()
            AbstractMigration.logger('Finish migration %s.', self.MIGRATION_KEY)
        AbstractMigration.logger('-'*50)

    def _execute_migration(self):
        raise NotImplementedError()
