#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys

from app import settings
from app.db.postgresql import settings as postgresql_settings

from argparse import ArgumentParser


try:
    command = sys.argv[1]
except IndexError:
    command = 'help'

print command

if command == 'help':
    print 'all commands are dsf,fdg,fd'
elif command=='ttt':

    arguments = ArgumentParser(
        prog='MyApplicetion',
        description='description',
        epilog='epilog'
    )
    arguments.add_argument(
        '-t',
        '--test_command',
        default=4,
        type=int,
        action='store',
        help='any param',
    )
    command = arguments.parse_args(sys.argv[2:])
else:
    print 'all commands are dsf,fdg,fd'


# if not console.command:
    # arguments.print_help()
    # exit(0)
# else:
    # import ipdb; ipdb.set_trace()
    # print console.test_command
    # print type(console.test_command)
    # print '1'* 10
    # print console.command
    # print type(console.command)


