import requests
import traceback
import helper.utils as utils

from requests.cookies import RequestsCookieJar

from api.http_request import Request
from api.http_response import HttpResponse
from api.http_method import HttpMethod
from abc import ABC


class VodafoneBase(ABC):

    def __init__(self, gateway: str):
        self.__gateway = gateway
        self.__cookies = {}

    def _query(self, method: str, request: Request, token: str = None) -> HttpResponse:
        headers = self.__build_headers(token)
        url = self.__build_url(request.url_path)
        data = request.body if method != HttpMethod.GET else None
        try:
            response = requests.request(method, url, headers=headers, data=data, cookies=self.__cookies)
            if response.status_code == requests.codes.ok:
                self.cookies = response.cookies
            return HttpResponse(response.json())
        except requests.exceptions.RequestException:
            traceback.print_exc()
        return HttpResponse()

    def __build_url(self, url_path: str):
        return f'http://{self.__gateway}{url_path}'

    @staticmethod
    def __build_headers(token: str):
        return {'X-Requested-With': 'XMLHttpRequest', 'X-CSRF-Token': token}

    @property
    def cookies(self):
        return self.__cookies

    @cookies.setter
    def cookies(self, cookies: RequestsCookieJar):
        self.__cookies |= cookies

    @staticmethod
    def create_pbkdf2_pass(password: str, salt: str, salt_web: str) -> str:
        password = utils.create_pbkdf2(password, salt)
        return utils.create_pbkdf2(password, salt_web)
