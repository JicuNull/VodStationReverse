from abc import ABC, abstractmethod


class Request(ABC):

    def __init__(self, body: dict = None):
        self.__body = body

    @property
    def body(self) -> dict:
        return self.__body

    @property
    @abstractmethod
    def url_path(self) -> str:
        pass


class SeekSaltRequest(Request):

    def __init__(self):
        super().__init__({'username': 'admin', 'password': 'seeksalthash', 'logout': 'true'})

    @property
    def url_path(self) -> str:
        return '/api/v1/session/login'


class LoginRequest(Request):

    def __init__(self, password: str):
        super().__init__({'username': 'admin', 'password': password})

    @property
    def url_path(self) -> str:
        return '/api/v1/session/login'


class MenuRequest(Request):

    @property
    def url_path(self) -> str:
        return '/api/v1/session/menu'


class FirewallRequest(Request):

    def __init__(self, toggle: bool = False):
        super().__init__({'FirewallLevel': 'on' if toggle else 'off', 'FirewallLevelV6': 'on' if toggle else 'off'})

    @property
    def url_path(self) -> str:
        return '/api/v1/firewall'


class DeviceRequest(Request):

    def __init__(self, led: bool = False, http_state: bool = False):
        super().__init__({'led': led, 'http_state': http_state})

    @property
    def url_path(self) -> str:
        return '/api/v1/set_device/Sdevice'


class DeviceTokenRequest(Request):

    @property
    def url_path(self) -> str:
        return '/api/v1/set_device'
