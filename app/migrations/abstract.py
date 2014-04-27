#-*- coding: utf-8 -*-
import os
from app import settings as app_settings
from app.db import get_connection


class AbstractMigration(object):

    MIGRATION_KEY = None
    DB_KEY = 'default'

    @property
    def conn(self):
        return get_connection(self.DB_KEY)

    def execute_raw_sql(self, sql_file_path):
        full_path = app_settings.PROJECT_ROOT + sql_file_path
        if not os.path.isfile(full_path):
            raise Exception('File %s does not exists' % full_path)


        with open(full_path, 'r') as f:
            sql_commands = f.read()
            cursor = self.conn.cursor()
            print '  Execute raw_sql file: %s' % full_path
            print '  File content is: \n%s' % sql_commands

            try:
                cursor.execute('BEGIN')
                cursor.execute(sql_commands)
                cursor.execute('COMMIT')
            except:
                cursor.execute('ROLLBACK')
                raise
            else:
                self._mark_migration_as_executed()

            self.conn.commit()

    def _is_migration_executed(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT 1 from pg_tables WHERE tablename=%s', ('migrations', ))
        if not cursor.rowcount:
            #it's first init migration
            return False

        cursor.execute('SELECT * FROM migrations WHERE key=%s', (
            self.MIGRATION_KEY,
        ))
        if cursor.rowcount:
            print '  Migration %s was executed %s.' %  (
                self.MIGRATION_KEY,
                cursor.fetchone()['created_at'],
            )
            return True
        return False

    def _mark_migration_as_executed(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO migrations (key) values (%s)', (
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
            AbstractMigration.logger('Migration %s is wrong.', self.__class__)
            raise Exception('MIGRATION_KEY is not defined. Check your migration class')

        if self._is_migration_executed():
            print '  Skipped.'
            return

        AbstractMigration.logger('Run migration %s.', self.MIGRATION_KEY)
        self._execute_migration()
        AbstractMigration.logger('Finish migration %s.', self.MIGRATION_KEY)
        AbstractMigration.logger('-'*50)


    def _execute_migration(self):
        raise NotImplementedError()
