import unittest
import json
import yaml

from common.request_handler import RequestsHandler
from common.excel_handler import ExcelHandler
from common.logger_handler import LoggerHandler
from common.db_handler import DBHandler
from libs import ddt
from config.setting import Config, DevConfig
from middleware.helper import save_token, Context

f = open(Config.yaml_config_path, encoding='utf-8')
yaml_data = yaml.load(f, Loader=yaml.FullLoader)
print(yaml_data)


@ddt.ddt
class TestInvest(unittest.TestCase):
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
        # 结果
        # save_token() 不这么用了  用propery
        # save_loan_id()
        # token = Context.token
        # member_id = Context.member_idt


    def tearDown(self) -> None:
        self.req.close_session()
        self.db.close()

    @ddt.data(*data)
    def test_invest(self, test_data):

        # 替换动态的数据
        token = Context().token
        member_id = Context().member_id
        loan_id = Context().loan_id


        # 查询数据库
        sql = 'select * from member where id =%s;'
        user = self.db.query(sql, args=[member_id])
        before_money = user['leave_amount']

        # 判断 #exist_phone#
        if '#member_id#' in test_data['json']:
            test_data['json'] = test_data['json'].replace("#member_id#", str(member_id))

        if '#wrong_member#' in test_data['json']:
            test_data['json'] = test_data['json'].replace("#wrong_member#", str(member_id + 1))

        # 在原headers+token 添加Authorization
        headers = json.loads(test_data['headers'])
        headers['Authorization'] = token

        # 得到实际结果
        res = self.req.visit(DevConfig.host + test_data['url'],
                             test_data['method'],
                             json=json.loads(test_data['json']),
                             headers=headers)

        # 断言1:返回码
        self.assertEqual(res['code'], test_data['expected'])
        # 断言2：余额 成功用例要进行数据库校验
        # 判断是否为成功用例，校验数据库
        # if test_data['tag'] == 'success'
        if res['code'] == 0:
            # 查看数据库结果， 剩余金额-投资金额 == 投资后的金额
            # 投资金额
            money = json.loads(test_data['json'])['amount']
            # 获取投资前的金额

            # 获取投资之后的金额
            sql = 'select * from member where id =%s;'
            after_user = self.db.query(sql, args=[member_id])
            after_money = after_user['leave_amount']

            self.assertEqual(before_money - money, after_money)

        try:
            self.assertEqual()
            # 写入excel数据
            self.excel_handle.write(Config.data_path, 'Invest',
                                    test_data['case_id'] + 1,
                                    9,
                                    "测试通过")
        except AssertionError as e:
            # 记录logger
            self.logger.error("测试用例失败,{}".format(e))
            self.excel_handle.write(Config.data_path, 'Invest',
                                    test_data['case_id'] + 1,
                                    9,
                                    "测试失败")
            # 一定要抛异常 否则测试用例自动通过
            raise e
