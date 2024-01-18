from dadata_api_tests_framework.utils.attach import api_request


class MetroApi:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def find_metro_station(self, query, city=None, line_id=None, is_closed=None):
        filters = {"city": city, "line_id": line_id, "is_closed": is_closed}
        data = {"query": query, "filters": [i for i in [filters] if any(i.values())]}

        return api_request(self.base_url + '/suggest/metro', '', 'post', self.headers, json=data)
