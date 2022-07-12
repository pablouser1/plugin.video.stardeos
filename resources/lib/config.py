from xbmcaddon import Addon

class Config:
    addon = Addon('plugin.video.stardeos')

    def getLocalizedString(self, l_id: int)-> str:
        return self.addon.getLocalizedString(l_id)

    # Comprueba si el usuario ya ha iniciado sesión
    def hasLoginData(self)-> bool:
        if self.addon.getSettingString('access_token'):
            return True
        return False

    def getToken(self)-> str:
        access = self.addon.getSettingString('access_token')
        return access

    def getUserId(self)-> str:
        return self.addon.getSettingString('user_id')

    def getVersion(self) -> str:
        return self.addon.getAddonInfo('version')

    def setAuth(self, access_token: str, username: str, user_id: str):
        self.addon.setSettingString('access_token', access_token)
        self.addon.setSettingString('username', username)
        self.addon.setSettingString('user_id', user_id)
