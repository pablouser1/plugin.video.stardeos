import xbmcgui
from .Base import Base
from ..common import api, params

class Channel(Base):
    """
    Get videos from Channel username
    """
    pagination = True

    def setItems(self):
        if not self.term:
            username = xbmcgui.Dialog().input('Type the channel username', type=xbmcgui.INPUT_ALPHANUM)
            if username:
                self.term = username
        self.items = api.channel(self.term, self.page)
