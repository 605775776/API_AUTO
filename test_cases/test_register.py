import unittest
import json
import yaml

from common.request_handler import RequestsHandler
from common.excel_handler import ExcelHandler
from common.logger_handler import LoggerHandler

from libs import ddt
from config.setting import Config

# ddt ==> data driven testing 数据驱动思想
# ddt 的库 要和unittest组合使用

from common.yaml_handler import YamlHandler

# test_data = ExcelHandler(r'd:\case_data.xlsx', 'Sheet1').read()

# yaml 读取
f = open(Config.yaml_config_path, encoding='utf-8')
yaml_data = yaml.load(f, Loader=yaml.FullLoader)
print(yaml_data)


@ddt.ddt
class TestRegister(unittest.TestCase):

    # 读取数据
    excel_handle = ExcelHandler(Config.data_path, 'Register')
    test_data = excel_handle.read()

    # 读取日志级别
    name = yaml_data['logger']['name']
    level = yaml_data['logger']['level']
    file = yaml_data['logger']['file']

    logger = LoggerHandler(name, level, file)



    # 传入文件名等 config文件中
    # name = YamlHandler(Config.yaml_config_path).read_yaml()['logger']['name']
    # level = YamlHandler(Config.yaml_config_path).read_yaml()['logger']['level']
    #
    # file = YamlHandler(Config.yaml_config_path).read_yaml()['logger']['file']




    def setUp(self) -> None:
        self.req = RequestsHandler()
    def tearDown(self) -> None:
        self.req.close_session()

    # 还是要分开 独立测试用例 但是逻辑重复 要应用数据驱动
    # *test_data 当中的一组测试数据，赋值到data_info这个参数
    @ddt.data(*test_data)
    def test_register(self, test_data):
        # print(type(eval(data_info['headers'])))
        res = self.req.visit(Config.host + test_data['url'],
                             test_data['method'],
                             json = json.loads(test_data['json']),
                             headers = json.loads(test_data['headers']))
        try:
            self.assertEqual(test_data['expected'], res['code'])
        except AssertionError as e:
            self.logger.error("测试用例失败", e)

            # 一定要抛异常 否则测试用例自动通过
            raise e

