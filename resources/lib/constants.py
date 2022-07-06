def __enum(**enums):
    return type('Enum', (), enums)

ROUTES = __enum(
    HOME='home',
    LOGIN='login',
    LOGOUT='logout',
    SEARCH='search',
    CATALOG='catalog',
    PLAYER='player'
)
