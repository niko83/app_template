#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys

from app import settings
from app.db.postgresql import settings as postgresql_settings

from argparse import ArgumentParser

arguments = ArgumentParser(
    prog='prog',
    description='desc',
    epilog='info')

arguments.add_argument(
    '-t', '--test_command',
    action='test',
    version='Test command'
)

console = arguments.parse_args(sys.argv[1:])

print console.test
