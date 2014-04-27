from .abstract import AbstractMigration


class Migration(AbstractMigration):

    MIGRATION_KEY = 'create_migrations_table'

    def _execute_migration(self):
        self.execute_raw_sql('app/migrations/sql/0001.sql')
