from collections import namedtuple


__all__ = ('DEFINES',)


Setting = namedtuple(typename='Setting', field_names=('name', 'content_type', 'default', 'description'))


DEFINES = (
    Setting(name='DEBUG', content_type=bool, default=True, description="Enable debug mode."),
    Setting(name='PORT', content_type=int, default=8000, description="Port, default: 8000."),
)
