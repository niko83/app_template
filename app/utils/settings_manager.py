from app import settings as app_settings, Settings


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
