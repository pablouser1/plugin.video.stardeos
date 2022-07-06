import requests
from .exceptions.ApiException import ApiException

class Api:
    BASE_URL = "https://stardeos.com/api/v2"
    s = requests.Session()

    def __init__(self):
        self.s.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
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

    def makeRequest(self, endpoint: str, method = 'GET', body: dict = {}, query: dict = {}, headers: dict = {}):
        res = self.s.request(method, self.BASE_URL + endpoint, json=body, params=query, headers=headers)
        if res.ok and res.headers['Content-Type'] == 'application/json; charset=utf-8':
            return res.json()
        raise ApiException('Api error')

    def login(self, username: str, password: str)-> dict:
        res = self.makeRequest('/auth/login', 'POST', {
            "password": password,
            "username": username
        }, headers={
            "Origin": "https://stardeos.com",
            "Referer": "https://stardeos.com/login"
        })
        return res

    def setToken(self, token: str):
        self.s.headers["Authorization"] = f'Bearer {token}'

    def getUserAgent(self):
        return self.s.headers['User-Agent']

    def catalog(self):
        res = self.makeRequest('/videos', query={
            'filter': 'LATEST'
        }, headers={
            'Referer': 'https://stardeos.com'
        })
        return res

    def search(self, term: str) -> dict:
        res = self.makeRequest('/videos/browse', query={
            'q': term,
            'page': 1
        }, headers={
            "Referer": "https://stardeos.com/?q=" + term
        })

        return res

    def video(self, vid_id: int) -> dict:
        res = self.makeRequest('/videos/' + vid_id, headers={
            'Referer': 'https://stardeos.com/video/' + vid_id
        })

        return res
