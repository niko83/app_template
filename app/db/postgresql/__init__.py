from app.utils.settings_manager import update_settings

class Settings(object):
    POOL = {}

settings = Settings()
update_settings('DB_POSTGRESQL_', settings)

