import unittest
import json
import yaml

from common.request_handler import RequestsHandler
from common.excel_handler import ExcelHandler
from common.logger_handler import LoggerHandler
from common.db_handler import DBHandler
from libs import ddt
from config.setting import Config, DevConfig

f = open(Config.yaml_config_path, encoding='utf-8')
yaml_data = yaml.load(f, Loader=yaml.FullLoader)
print(yaml_data)


@ddt.ddt
class TestRecharge(unittest.TestCase):
    # 读取数据
    excel_handle = ExcelHandler(Config.data_path, 'Recharge')
    data = excel_handle.read()

    # 读取日志级别
    name = yaml_data['logger']['name']
    level = yaml_data['logger']['level']
    # file = yaml_data['logger']['file']
    file = Config.log_path + '\\' + yaml_data['logger']['file']
    logger = LoggerHandler(name, level, file)

    def setUp(self) -> None:
        self.req = RequestsHandler()
        self.db = DBHandler(host=yaml_data['database']['host'],
                            port=yaml_data['database']['port'],
                            user=yaml_data['database']['user'],
                            password=yaml_data['database']['password'],
                            charset=yaml_data['database']['charset'],
                            database=yaml_data['database']['database'])
        # 登录



    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_recharge(self, test_data):

        res = self.req.visit(DevConfig.host + test_data['url'],
                             test_data['method'],
                             json=json.loads(test_data['json']),
                             headers=json.loads(test_data['headers']))
        try:
            self.assertEqual()
            # 写入excel数据
            self.excel_handle.write(Config.data_path, 'Register',
                                    test_data['case_id'] + 1,
                                    9,
                                    "测试通过")
        except AssertionError as e:
            # 记录logger
            self.logger.error("测试用例失败,{}".format(e))
            self.excel_handle.write(Config.data_path, 'Register',
                                    test_data['case_id'] + 1,
                                    9,
                                    "测试失败")
            # 一定要抛异常 否则测试用例自动通过
            raise e
