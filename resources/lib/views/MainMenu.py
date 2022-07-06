from .Base import Base
from ..common import config

class MainMenu(Base):
    """
    Main menu, default menu. Does not have a path string
    """
    static = True
    items = [
        {
            "id": "catalog",
            "title": config.getLocalizedString(50011)
        },
        {
            "id": "search",
            "title": config.getLocalizedString(50012)
        }
    ]
