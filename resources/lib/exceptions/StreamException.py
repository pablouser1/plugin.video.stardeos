from xbmcgui import Dialog
from ..common import config

class StreamException(Exception):
    """
    TODO
    Throw exception when not allowed to stream
    """
    def __init__(self, errors: str):
        super().__init__()
        Dialog().ok('Stardeos API Error', config.getLocalizedString(50011))
