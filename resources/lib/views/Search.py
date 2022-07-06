import xbmcgui
from .Base import Base
from ..common import api, config

class Search(Base):
    """
    Search function
    """
    pagination = True

    def setItems(self):
        if not self.term:
            search_term = xbmcgui.Dialog().input(config.getLocalizedString(50012), type=xbmcgui.INPUT_ALPHANUM)
            if search_term:
                self.term = search_term
        self.items = api.search(self.term, self.page)
