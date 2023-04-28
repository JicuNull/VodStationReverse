class HttpResponse:

    def __init__(self, body: dict = None):
        self.__body = body if not None else {'error': 'error'}

    @property
    def body(self):
        return self.__body

    def success(self):
        return 'error' in self.__body and self.__body['error'] == 'ok'
