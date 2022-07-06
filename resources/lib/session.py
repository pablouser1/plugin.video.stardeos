from xbmcgui import Dialog
from .common import api, config

def askLogin():
    username = Dialog().input(config.getLocalizedString(50008))
    password = Dialog().input(config.getLocalizedString(50009))
    if username and password:
        res = api.login(username, password)
        api.setToken(res['data']['access_token'])
        user = res['data']['user']
        config.setAuth(res['data']['access_token'], username, user['_id'])
        Dialog().ok('Login', config.getLocalizedString(50010))

def startLogout():
    config.setAuth('', '', '')
    api.setToken('')
    Dialog().ok('Done', 'Logged out')
