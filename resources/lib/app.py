from .routes import dispatch
from .common import config, api, params

def run():
    # Check if user already has a session
    if config.hasLoginData():
        token = config.getToken()
        api.setToken(token)

    dispatch()
