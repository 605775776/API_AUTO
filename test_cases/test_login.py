import unittest
import warnings
from common.request_handler import RequestsHandler
from common.excel_handler import ExcelHandler
# ddt ==> data driven testing 数据驱动思想
# ddt 的库 要和unittest组合使用
from common.excel_handler import ExcelHandler
import ddt
from libs import ddt
test_data = ExcelHandler(r'd:\case_data.xlsx', 'Sheet1').read()


@ddt.ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        warnings.simplefilter('ignore', ResourceWarning)

    def tearDown(self) -> None:
        pass

    # 还是要分开 独立测试用例 但是逻辑重复 要应用数据驱动
    # *test_data 当中的一组测试数据，赋值到data_info这个参数
    @ddt.data(*test_data)
    def test_login(self, data_info):
        # print(type(eval(data_info['headers'])))

        res = RequestsHandler().visit(data_info['url'],
                                      data_info['method'],
                                      json=eval(data_info['data']),
                                      headers=eval(data_info['headers']))


        self.assertEqual(res['code'], data_info['expected'])

