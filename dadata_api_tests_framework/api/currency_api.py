from dadata_api_tests_framework.utils.attach import api_request


class CurrencyApi:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def api_call(self, query):
        data = {"query": query}
        return api_request(self.base_url + '/findById/currency', '', 'post', self.headers, json=data)
