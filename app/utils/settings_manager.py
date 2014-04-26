from app import settings as app_settings, Settings
from app.commands.abstract import AbstractCommand
import sys


@property
def _closed_attr(self):
    raise NotImplementedError()


def update_settings(prefix, settings):
    for attr in dir(settings):
        long_attr_name = prefix + attr
        if hasattr(app_settings, long_attr_name):
            setattr(
                settings,
                attr,
                getattr(app_settings, long_attr_name)
            )
            setattr(Settings, long_attr_name, _closed_attr)


def get_available_commands():
    raise NotImplementedError


def get_command_class(command_name):

    if not command_name:
        return

    for patch in app_settings.INCLUDED_PATCH_FOR_SEARCH_COMMANDS:
        full_patch = patch + '.' + command_name
        try:
            __import__(full_patch)
            module = sys.modules[full_patch]
        except (ImportError, KeyError):
            continue

        for entity_str in dir(module):
            if entity_str.startswith('__'):
                continue

            entity = getattr(module, entity_str)

            if entity != AbstractCommand and issubclass(entity, AbstractCommand):
                return entity
