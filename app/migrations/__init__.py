#-*- coding: utf-8 -*-

u"""
Модуль предназначен для миграция данных, обновление схемы базы данных.

Поддерживает выполенение миграций оформленных в виде raw sql  в отдельном файле,
inline row sql, а также какой-либо выполнение логики на стороне python
c последующим обновлением таблиц.

Для использования механизма миграций необходимо:
  * Создать файл  миграции, реализущий интерфейс ``app.commands.abstract.AbstractCommand``
    Пример ::

      from app.migrations.abstract import AbstractMigration
      class Migration(AbstractMigration):
          MIGRATION_KEY = 'create_migrations_table'
          def _execute_migration(self):
              self.apply_raw_sql_file('app/migrations/sql/0001.sql')
              self.execute_sql('INSERT INTO test_table (id) VALUES (123)')

  * Зарегистрировать миграцию в ``app.settings.MIGRATIONS`` ::

      MIGRATIONS = (
          'app.any_module.MyMigration',
      )

Выолнить миграции для проекта можно командой ``./console.py migrate``

в DB таблице ``migrations`` фиксируются какие когда  миграции выполнялись
"""
