from utils.attach import api_request


class CurrencyAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def api_call(self, query):
        data = {"query": query}
        return api_request(self.base_url, '', 'post', self.headers, json=data)


