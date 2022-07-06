from ..helpers.Render import Render

class Base:
    """
    Main view class, skeleton for all views
    """

    term = ''

    """
    Set to True if the endpoint has a pagination system
    """
    pagination = False

    """
    Current page
    """
    page = 1

    """
    True if is an static menu with predefined items
    """
    static = False

    """
    All items
    """
    items = []

    def __init__(self, page = 1, term = ''):
        if self.pagination:
            self.page = page

        if term:
            self.term = term

    def setItems(self):
        """
        Set item using API if necessary
        """
        pass

    def show(self):
        """
        Renders folder depending of config
        """
        listing = []
        # Render static menu
        if self.static:
            listing = Render.static(self.items)
        else:
            listing = Render.videos(self.items, self.pagination, self.term)

        Render.createDirectory(listing)

    def run(self):
        self.setItems()
        self.show()
