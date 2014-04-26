#-*- coding: utf-8 -*-


class AbstractCommand(object):

    def __init__(self, arguments, command_args):
        self.arguments = arguments.parse_args(command_args)

    def run(self):
        raise NotImplementedError()
