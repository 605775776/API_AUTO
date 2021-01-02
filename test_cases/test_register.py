import unittest
import json
import yaml

from common.helper import generate_mobile
from common.request_handler import RequestsHandler
from common.excel_handler import ExcelHandler
from common.logger_handler import LoggerHandler

from libs import ddt
from config.setting import Config,DevConfig

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
    data = excel_handle.read()

    # 读取日志级别
    name = yaml_data['logger']['name']
    level = yaml_data['logger']['level']
    file = yaml_data['logger']['file']

    logger = LoggerHandler(name, level, file)

    def setUp(self) -> None:
        self.req = RequestsHandler()

    def tearDown(self) -> None:
        self.req.close_session()

    # 还是要分开 独立测试用例 但是逻辑重复 要应用数据驱动
    # *test_data 当中的一组测试数据，赋值到data_info这个参数
    @ddt.data(*data)
    def test_register(self, test_data):

        # 判断 #exist_phone#
        if '#exist_phone#' in test_data['json']:
            mobile = generate_mobile()

            # 直接查询数据库 随机找一个 直接使用该号码替换
            # mobile = db.find('select')
        # 判断 #new_phone#
            if '#new_phone#' in test_data['json']:
                while True:
                    mobile = generate_mobile()
                    # 查数据库 若存在 再生成一个 直到数据库中不存在为止
                    # mobile = db.find('select')
            test_data['json'] = test_data['json'].replace("#exist_phone#", mobile)
        res = self.req.visit(DevConfig.host + test_data['url'],
                             test_data['method'],
                             json=json.loads(test_data['json']),
                             headers=json.loads(test_data['headers']))
        try:
            self.assertEqual(test_data['expected'], res['code'])

            # 写入excel数据
            self.excel_handle.write(Config.data_path, 'Register',
                                    test_data['case_id'] + 1,
                                    9,
                                    "测试通过")
        except AssertionError as e:
            # 记录logger
            self.logger.error("测试用例失败", e)
            self.excel_handle.write(Config.data_path, 'Register',
                                    test_data['case_id'] + 1,
                                    9,
                                    "测试失败")

            # 一定要抛异常 否则测试用例自动通过
            raise e

