from .dispatcher import Dispatcher
from .constants import ROUTES
from .common import params

dispatcher = Dispatcher()

@dispatcher.register(ROUTES.HOME)
def _home():
    from .views.MainMenu import MainMenu
    MainMenu().run()

@dispatcher.register(ROUTES.LOGIN)
def _login():
    from .session import askLogin
    askLogin()

@dispatcher.register(ROUTES.LOGOUT)
def _logout():
    from .session import startLogout
    startLogout()

@dispatcher.register(ROUTES.TRENDING, kwargs=['page'])
def _trending(page: int = 1, term: str = ""):
    from .views.Videos import Videos
    Videos(page, 'TRENDING').run()

@dispatcher.register(ROUTES.LATEST, kwargs=['page'])
def _latest(page: int = 1):
    from .views.Videos import Videos
    Videos(page, 'LATEST').run()

@dispatcher.register(ROUTES.FOLLOWING, kwargs=['page'])
def _following(page: int = 1):
    from .views.Videos import Videos
    Videos(page, 'FOLLOWING').run()

@dispatcher.register(ROUTES.RECOMMENDED, kwargs=['page'])
def _recommended(page: int = 1):
    from .views.Videos import Videos
    Videos(page, 'RECOMMENDED').run()

@dispatcher.register(ROUTES.CHANNEL, kwargs=['page', 'term'])
def _channel(page: int = 1, term: str = ""):
    from .views.Channel import Channel
    Channel(page, term).run()

@dispatcher.register(ROUTES.SEARCH)
def _search(page: int = 1, term: str = ""):
    from .views.Search import Search
    Search(page, term).run()

@dispatcher.register(ROUTES.PLAYER, ['id'])
def _player(item_id: int):
    from .helpers.Player import Play
    play = Play(item_id)
    play.start()

def dispatch():
    mode = params.get('menu', 'home')
    dispatcher.run(mode)
