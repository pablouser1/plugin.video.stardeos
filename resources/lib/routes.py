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

@dispatcher.register(ROUTES.CATALOG)
def _catalog():
    from .views.Catalog import Catalog
    Catalog().run()

@dispatcher.register(ROUTES.SEARCH)
def _search():
    from .views.Search import Search
    Search().run()

@dispatcher.register(ROUTES.PLAYER, ['id'])
def _player(item_id: int):
    from .player.Handler import Play
    play = Play(item_id)
    play.start()

def dispatch():
    mode = params.get('menu', 'home')
    dispatcher.run(mode)
