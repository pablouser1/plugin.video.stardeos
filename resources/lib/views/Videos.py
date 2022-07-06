from .Base import Base
from ..common import api, config

class Videos(Base):
    """
    /videos endpoint
    """
    pagination = True

    def setItems(self):
        self.items = api.videos(self.term, config.getUserId(), self.page)
