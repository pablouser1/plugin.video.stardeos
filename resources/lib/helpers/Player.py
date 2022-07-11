from xbmcplugin import setResolvedUrl
from ..common import api, _HANDLE
from ..helpers.listitem import setInfoVideo

class Play():
    item = {}

    def __init__(self, vid_id: int):
        self.item = api.video(vid_id)

    def start(self):
        # User-Agent personalizado (No sé hasta que punto es necesario)
        url = self.item['video'] + f'|User-Agent:{api.getUserAgent()}|'

        play_item = setInfoVideo(url, self.item)
        setResolvedUrl(_HANDLE, True, play_item)
