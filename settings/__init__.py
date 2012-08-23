from .base import *

servers = {
    'development': [
        'steven-desktop',
    ],
    'testing': [

    ],
    'production': [
        's8.wservices.ch',
    ]
}

def get_server_type():
    from socket import gethostname
    server_name = gethostname()
    for server_type, names in servers.items():
        if server_name in names:
            return server_type

    return 'testing' # default server type. This way
    # not all testing servers have to be listed above

exec("from %s import *" % get_server_type())

try:
    from .local import *
except ImportError:
    pass
