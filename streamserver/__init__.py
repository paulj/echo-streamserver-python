# -*- coding: utf-8 -*-

"""
Echo StreamServer API library
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2012 by About Echo
:license: ISC, see LICENSE for more details.

"""

__title__ = 'streamserver'
__version__ = '0.0.1'
__build__ = 0x000001
__author__ = 'Paul Jones'
__license__ = 'ISC'
__copyright__ = 'Copyright 2012 About Echo'

from .items_client import ItemsClient
from .feeds_client import FeedsClient
from .users_client import UsersClient
from .kv_client import KVClient
from .echo_client import (EchoAuthMethod, EchoAuthConfig)
from .exceptions import *