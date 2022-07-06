from .Base import Base
from ..common import config

class MainMenu(Base):
    """
    Main menu, default menu.
    """
    static = True
    items = [
        {
            "id": "search",
            "title": config.getLocalizedString(50012)
        },
        {
            "id": "recommended",
            "title": config.getLocalizedString(50017)
        },
        {
            "id": "following",
            "title": config.getLocalizedString(50016)
        },
        {
            "id": "trending",
            "title": config.getLocalizedString(50014)
        },
        {
            "id": "latest",
            "title": config.getLocalizedString(50015)
        },
        {
            "id": "channel",
            "title": config.getLocalizedString(50013)
        }
    ]
