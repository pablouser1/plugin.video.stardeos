import xbmcgui
import xbmcplugin

from ..common import _HANDLE, _URL, params
from .listitem import setInfoVideo, setInfoFolder
from urllib.parse import urlencode

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
    def videos(items: dict, pagination: bool, term: str)-> list:
        """
        Render videos fetched from Stardeos API
        """
        listing = []
        if items:
            for item in items['videos']:
                url = '{0}?menu=player&id={1}'.format(_URL, item["id"])
                list_item = setInfoVideo(url, item)
                list_item.setProperty('IsPlayable', 'true')
                listing.append((url, list_item, False))
            if pagination:
                if items['meta']['next']:
                    params['page'] = int(items['meta']['page']) + 1
                    url_next = _URL + '?' + urlencode(params)
                    if term:
                        url_next += '&term=' + term
                    list_item = setInfoFolder(url_next, "Next")
                    listing.append((url_next, list_item, True))
        return listing

    @staticmethod
    def createDirectory(listing: list):
        """
        Append folder to Kodi
        """
        xbmcplugin.addDirectoryItems(_HANDLE, listing, len(listing))
        xbmcplugin.addSortMethod(_HANDLE, xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.endOfDirectory(_HANDLE)
