import unittest
import requests

class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.login_url = "http://120.78.128.25:8766/futureloan/member/login"
        self.data = {"mobile_phone": "15745612312", "pwd": "12345612"}
        self.header = {"X-Lemonban-Media-Type": "lemonban.v2"}


    def tearDown(self) -> None:
        pass

    def test_login_success(self):
        res_login = requests.post(self.login_url, json=self.data, headers=self.header)
        try:
            self.assertEqual("OK", res_login.json()['msg'])
        except AssertionError as e:
            print("断言失败", e)
            raise AssertionError