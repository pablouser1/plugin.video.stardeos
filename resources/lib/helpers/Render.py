import xbmcgui
import xbmcplugin

from ..common import _HANDLE, _URL, params
from .listitem import setInfoVideo, setInfoFolder

class Render:
    @staticmethod
    def static(items: list)-> list:
        """
        Render static folders
        """
        listing = []
        for item in items:
            list_item = xbmcgui.ListItem(label=item["title"])
            info = {
                "title": item["title"]
            }
            url = '{0}?menu={1}'.format(_URL, item["id"])
            list_item.setInfo('video', info)
            listing.append((url, list_item, True))

        return listing

    @staticmethod
    def videos(items: list)-> list:
        """
        Render videos fetched from Stardeos API
        """
        listing = []
        for item in items['videos']:
            url = '{0}?menu=player&id={1}'.format(_URL, item["id"])
            list_item = setInfoVideo(url, item)
            list_item.setProperty('IsPlayable', 'true')
            listing.append((url, list_item, False))
        return listing

    @staticmethod
    def folders(items: list, menu: str = '')-> list:
        """
        Render folders fetched from Stardeos API
        """
        listing = []
        for item in items:
            url = '{0}?menu={1}&id={2}'.format(_URL, menu, item["id"])
            list_item = setInfoFolder(url, item)
            listing.append((url, list_item, True))
        return listing

    @staticmethod
    def createDirectory(listing: list):
        """
        Append folder to Kodi
        """
        xbmcplugin.addDirectoryItems(_HANDLE, listing, len(listing))
        xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(_HANDLE)
