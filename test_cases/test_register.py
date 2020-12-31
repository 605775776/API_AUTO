import unittest
import json
import warnings
from common.request_handler import RequestsHandler
from common.excel_handler import ExccelHandler
# ddt ==> data driven testing 数据驱动思想
# ddt 的库 要和unittest组合使用
from common.excel_handler import ExccelHandler
import ddt
from libs import ddt
from common.yaml_handler import YamlHandler
from common.logger_handler import LoggerHandler
test_data = ExccelHandler(r'd:\case_data.xlsx', 'Sheet1').read()
from config.setting import Config


@ddt.ddt
class TestLogin(unittest.TestCase):

    # 读取数据
    excel_handle = ExccelHandler(Config.data_path)
    data = excel_handle.read('register')

    # 传入文件名等 config文件中
    logger = LoggerHandler(YamlHandler(Config.yaml_config_path).read_yaml())


    def setUp(self) -> None:
        self.req = RequestsHandler()
    def tearDown(self) -> None:
        self.req.close_session()

    # 还是要分开 独立测试用例 但是逻辑重复 要应用数据驱动
    # *test_data 当中的一组测试数据，赋值到data_info这个参数
    @ddt.data(*test_data)
    def test_register(self, data_info):
        # print(type(eval(data_info['headers'])))
        res = self.req.visit(Config.host + test_data['url'],
                             test_data['method'],
                             json = json.loads(test_data['json']),
                             headers = json.loads(test_data['headers']))
        try:
            self.assertEqual(test_data['expected'], res['code'])
        except AssertionError as e:

        #     print("测试用例通过")
        # except:
        #     print("测试用例不通过")

        # 断言失败 log

