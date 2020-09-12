from .common import *  # noqa

try:
    from .local import *  # noqa
except ModuleNotFoundError:
    print('No local.py found. Using production.py')
    from .production import *  # noqa
