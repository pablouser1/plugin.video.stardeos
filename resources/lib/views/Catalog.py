from .Base import Base
from ..common import api

class Catalog(Base):
    """
    Search function
    """
    path = 'catalog'
    has_videos = True

    def setItems(self):
        self.items = api.catalog()
