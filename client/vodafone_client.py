from client.vodafone_base import VodafoneBase
from api.http_response import HttpResponse
from api.http_method import HttpMethod
from api.http_request import *


class VodafoneClient(VodafoneBase):

    def __init__(self, gateway: str = '192.168.0.1'):
        super().__init__(gateway)

    def __seek_salt(self) -> HttpResponse:
        return self._query(HttpMethod.POST, SeekSaltRequest())

    def login(self, password: str) -> HttpResponse:
        response = self.__seek_salt()
        if not response.success():
            return response
        password = self.create_pbkdf2_pass(password, response.body['salt'], response.body['saltwebui'])
        response = self._query(HttpMethod.POST, LoginRequest(password))
        if response.success():
            self.get_menu()
        return response

    def toggle_firewall(self, enabled: bool) -> HttpResponse:
        token = self._query(HttpMethod.GET, FirewallRequest()).body.get('token')
        return self._query(HttpMethod.POST, FirewallRequest(enabled), token)

    def get_menu(self) -> HttpResponse:
        return self._query(HttpMethod.GET, MenuRequest())

    def toggle_led(self, enabled: bool) -> HttpResponse:
        response = self._query(HttpMethod.GET, DeviceTokenRequest())
        http = response.body.get('data', {}).get('http_state', False)
        token = response.body.get('token')
        return self._query(HttpMethod.POST, DeviceRequest(enabled, http), token)
