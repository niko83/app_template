#-*- coding: utf-8 -*-
import os

from .abstract import AbstractCommand
from app import settings as app_settings


def _psql_runshell(settings_dict):
    if app_settings.DEBUG:
        os.putenv('PGPASSWORD', settings_dict['PASSWORD'])
    executable_name = 'psql'
    args = [executable_name]
    if settings_dict['USER']:
        args += ["-U", settings_dict['USER']]
    if settings_dict['HOST']:
        args.extend(["-h", settings_dict['HOST']])
    if settings_dict['PORT']:
        args.extend(["-p", str(settings_dict['PORT'])])
    args += [settings_dict['NAME']]

    os.execvp(executable_name, args)


def _mysql_runshell(settings_dict):
    executable_name = 'mysql'
    args = [executable_name]

    if settings_dict['USER']:
        args += ["--user=%s" % settings_dict['USER']]
    if settings_dict['PASSWORD']:
        args += ["--password=%s" % settings_dict['PASSWORD']]

    if settings_dict['HOST']:
        if '/' in settings_dict['HOST']:
            args += ["--socket=%s" % settings_dict['HOST']]
        else:
            args += ["--host=%s" % settings_dict['HOST']]

    if settings_dict['PORT']:
        args += ["--port=%s" % settings_dict['PORT']]
    if settings_dict['NAME']:
        args += [settings_dict['NAME']]

    os.execvp(executable_name, args)


class Command(AbstractCommand):

    def __init__(self, arguments, command_args):
        arguments.add_argument(
            '--db',
            default='default',
            action='store',
            help='Choise db',
        )

        super(Command, self).__init__(arguments, command_args)

    def run(self):
        settings_dict = app_settings.DB.get(self.arguments.db)
        if settings_dict['ADAPTER'] == 'postgresql':
            runshell = _psql_runshell
        elif settings_dict['ADAPTER'] == 'mysql':
            runshell = _mysql_runshell

        runshell(settings_dict)
