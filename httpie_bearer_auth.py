"""
Bearer Auth plugin for HTTPie.

"""
from httpie.plugins import AuthPlugin

__version__ = '0.1.0'
__author__ = 'James Fenwick'
__licence__ = 'MIT'


class BearerAuth:
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'Bearer %s' % self.token
        return r


class BearerAuthPlugin(AuthPlugin):
    name = 'Bearer token auth'
    auth_type = 'bearer'
    auth_parse = True
    prompt_password = False
    description = 'Add a Bearer token to requests'

    def get_auth(self, username=None, password=None):
        return BearerAuth(password or username)
