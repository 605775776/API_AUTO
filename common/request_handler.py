import requests


class RequestsHandler:

    def __init__(self):
        self.session = requests.Session()

    def visit(self, url, method, params=None, data=None, json=None, **kwargs):
        res = self.session.request(method, url, params=params, data=data, json=json, **kwargs)
        try:
            return res.json()
        except ValueError:
            return "not json"

    def close_session(self):
        self.session.close()
