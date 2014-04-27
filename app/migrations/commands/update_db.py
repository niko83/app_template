#-*- coding: utf-8 -*-

from app.commands.abstract import AbstractCommand
from app import settings as app_settings
from app.utils.module_loading import import_by_path


class Command(AbstractCommand):

    def __init__(self, arguments, command_args):
        super(Command, self).__init__(arguments, command_args)

    def run(self):
        print '-' * 50
        for migration_str in app_settings.MIGRATIONS:
            migration_cls = import_by_path(migration_str)
            migration = migration_cls()
            migration.run()
        print "Success finish."
        print ""
