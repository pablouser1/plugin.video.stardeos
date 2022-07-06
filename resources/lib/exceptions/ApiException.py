from xbmcgui import Dialog

class ApiException(Exception):
    """
    Throw exception when HTTP code is diferent from 2XX
    """
    def __init__(self, errors: str):
        super().__init__()
        Dialog().ok('Stardeos API Error', errors)
