from jsonschema import validate


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json()
        self.status_code = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                validate(item, schema)
        else:
            validate(self.response_json, schema)

    def assert_status_code(self, expected_status_code):
        assert self.status_code == expected_status_code
        return self
