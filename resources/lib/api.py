import requests
from .exceptions.ApiException import ApiException

class Api:
    BASE_URL = "https://stardeos.com/api/v2"
    s = requests.Session()

    def __init__(self, version: str):
        self.s.headers.update({
            "User-Agent": f"Stardeos-For-Kodi/{version} (https://github.com/pablouser1/plugin.video.stardeos)",
            "Accept": "*/*",
            "Accept-Language": "es-ES",
            "Accept-Encoding": "gzip, deflate, br",
            "Cache-Control": "no-cache",
            "Content-Type": "application/json",
            "DNT": "1",
            "Connection": "keep-alive",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "TE": "trailers"
        })

    def makeRequest(self, endpoint: str, method='GET', body: dict = {}, query: dict = {}, headers: dict = {}):
        error = ''
        res = self.s.request(method, self.BASE_URL + endpoint,
                             json=body, params=query, headers=headers)
        if res.ok and res.headers.get('Content-Type', '') == 'application/json; charset=utf-8':
            return res.json()
        elif res.status_code == 403 and res.headers.get('Content-Type', '') == 'text/html; charset=UTF-8':
            error = 'Captcha detectado'
        else:
            error = 'Error desconocido'

        raise ApiException(error)

    def login(self, username: str, password: str) -> dict:
        res = self.makeRequest('/auth/login', 'POST', {
            "password": password,
            "username": username
        }, headers={
            "Origin": "https://stardeos.com",
            "Referer": "https://stardeos.com/login"
        })
        return res

    def videos(self, sort: str, userId: str = '', page: int = 1) -> dict:
        res = self.makeRequest('/videos', query={
            'filter': sort,
            'userId': userId,
            'page': page
        }, headers={
            'Referer': 'https://stardeos.com'
        })
        return res

    def channel(self, username: str, page: int = 1) -> dict:
        res = self.makeRequest('/channels/' + username + '/videos', query={
            'page': page
        }, headers={
            'Referer': 'https://stardeos.com/' + username
        })
        return res

    def search(self, term: str, page: int = 1) -> dict:
        res = self.makeRequest('/videos/browse', query={
            'q': term,
            'page': page
        }, headers={
            "Referer": "https://stardeos.com/?q=" + term
        })

        return res

    def video(self, vid_id: int) -> dict:
        res = self.makeRequest('/videos/' + vid_id, headers={
            'Referer': 'https://stardeos.com/video/' + vid_id
        })

        return res

    def setToken(self, token: str):
        self.s.headers["Authorization"] = f'Bearer {token}'

    def getUserAgent(self) -> str:
        return self.s.headers['User-Agent']
