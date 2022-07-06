def __enum(**enums):
    return type('Enum', (), enums)

ROUTES = __enum(
    HOME='home',
    LOGIN='login',
    LOGOUT='logout',
    SEARCH='search',
    TRENDING='trending',
    LATEST='latest',
    FOLLOWING='following',
    RECOMMENDED='recommended',
    CHANNEL='channel',
    PLAYER='player'
)
