#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys
from app.utils.settings_manager import get_command_class, get_available_commands

from argparse import ArgumentParser

arguments = ArgumentParser(
    prog='MyApplicetion',
    description='description',
    epilog='epilog'
)

command_name = None
command_args = []
try:
    command_name = sys.argv[1]
    command_args = sys.argv[2:]
except IndexError:
    pass

command_class = get_command_class(command_name)
if command_class:
    command = command_class(arguments, command_args)
    command.run()
else:
    print 'all commands are: %s' % ', '.join(get_available_commands())
