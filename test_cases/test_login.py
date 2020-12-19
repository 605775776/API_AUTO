import unittest
from common.request_handler import RequestsHandler
from common.excel_handler import ExccelHandler
# ddt ==> data driven testing 数据驱动思想
# ddt 的库 要和unittest组合使用
import ddt

test_data = [
    {"url": "http://120.78.128.25:8766/futureloan/member/login",
     "method": "post",
     "headers": {"X-Lemonban-Media-Type": "lemonban.v2"},
     "data": {"mobile_phone": "18111111111", "pwd": "12345678"},
     "expected": "hello world"
     },
]
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


    # 还是要分开 独立测试用例 但是逻辑重复 要应用数据驱动
    def test_login_success(self):
        data = test_data[0]
        res = RequestsHandler().visit(data['url'],
                                      data['method'],
                                      json=data['data'],
                                      headers=data['headers'])
        # try:
        self.assertEqual(res, data['expected'])
        #     print("测试用例通过")
        # except:
        #     print("测试用例不通过")
