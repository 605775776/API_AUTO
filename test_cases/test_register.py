import unittest
import json

from middleware.get_db import MyDBHandler
from middleware.helper import generate_mobile
from common.request_handler import RequestsHandler
from common.excel_handler import ExcelHandler
# from common.logger_handler import LoggerHandler
from middleware.get_logger import logger

from libs import ddt
from config.setting import Config, DevConfig
from middleware.yaml_handler import yaml_data
# ddt ==> data driven testing 数据驱动思想
# ddt 的库 要和unittest组合使用


@ddt.ddt
class TestRegister(unittest.TestCase):

    # 读取数据
    excel_handle = ExcelHandler(Config.data_path, 'Register')
    data = excel_handle.read()

    def setUp(self) -> None:
        self.req = RequestsHandler()
        self.db = MyDBHandler()

    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    # 还是要分开 独立测试用例 但是逻辑重复 要应用数据驱动
    # *data 当中的一组测试数据，赋值到test_data这个参数
    @ddt.data(*data)
    def test_register(self, test_data):

        # 判断 #exist_phone#
        if '#exist_phone#' in test_data['json']:
            # 直接查询数据库 随机找一个 直接使用该号码替换
            mobile = self.db.query("select * from member limit 1;")
            if mobile:
                test_data['json'] = test_data['json'].replace("#exist_phone#", mobile['mobile_phone'])
            else:
                # 随机生成一个 数据库不存在
                # 注册成功 helper方法
                pass
            # 判断 #new_phone#
            if '#new_phone#' in test_data['json']:
                while True:
                    gen_mobile = generate_mobile()
                    # 查数据库 若存在 再生成一个 直到数据库中不存在为止
                    mobile = self.db.query('select * from member where mobile_phone=%s;', args=[gen_mobile])
                    if not mobile:
                        break
                test_data['json'] = test_data['json'].replace("#new_phone#", gen_mobile)
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
            logger.error("测试用例失败,{}".format(e))
            self.excel_handle.write(Config.data_path, 'Register',
                                    test_data['case_id'] + 1,
                                    9,
                                    "测试失败")
            # 一定要抛异常 否则测试用例自动通过
            raise e

