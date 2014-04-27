# -*- coding: utf-8 -*-

from app.utils.settings_manager import update_settings

class Settings(object):
    pass

settings = Settings()
update_settings('DB_POSTGRESQL_', settings)
