import unittest
import warnings

from common.request_handler import RequestsHandler
from common.excel_handler import ExcelHandler
from config.setting import Config
from libs import ddt
from middleware.get_logger import logger



@ddt.ddt
class TestLogin(unittest.TestCase):
    # 读取数据
    excel_handle = ExcelHandler(Config.data_path, 'Register')
    data = excel_handle.read()


    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        pass

    # 还是要分开 独立测试用例 但是逻辑重复 要应用数据驱动
    # *data当中的一组测试数据，赋值到test_data这个参数
    @ddt.data(data)
    def test_login(self, test_data):
        res = RequestsHandler().visit(test_data['url'],
                                      test_data['method'],
                                      json=eval(test_data['data']),
                                      headers=eval(test_data['headers']))
        try:
            self.assertEqual(res['code'], test_data['expected'])
            # 写入excel数据
            self.excel_handle.write(Config.data_path, 'Login',
                                    test_data['case_id'] + 1,
                                    9,
                                    "测试通过")
        except AssertionError as e:
            # 记录logger
            logger.error("测试用例失败,{}".format(e))
            self.excel_handle.write(Config.data_path, 'Login',
                                    test_data['case_id'] + 1,
                                    9,
                                    "测试失败")
            # 一定要抛异常 否则测试用例自动通过
            raise e



