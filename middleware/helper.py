import random
import re
import yaml

from common.db_handler import DBHandler
from common.request_handler import RequestsHandler
from config.setting import Config
from jsonpath import jsonpath

# yaml 读取
f = open(Config.yaml_config_path, encoding='utf-8')
yaml_data = yaml.load(f, Loader=yaml.FullLoader)


def generate_mobile():
    "随机生成手机号码  1[3,5,8,9]+ 9"

    phone = '1' + random.choice(['3', '5', '8', '9'])
    for i in range(9):
        num = random.randint(0, 9)
        phone += str(num)
    return phone


def login():
    """登录，返回的是token 访问接口"""
    req = RequestsHandler()
    res = req.visit(Config.host + '/member/login',
                    'post',
                    json=yaml_data['user'],
                    headers={"X-Lemonban-Media-Type": "lemonban.v2"})
    return res

# Context().loan_id 读
# 上下文


class Context:
    # token = ""
    # member_id = None
    # leave_amount = 0

    @property
    def token(self):
        """token属性 而且属性会动态变化
        Context().token 获取token， 自动调用这个方法
        """
        data = login()
        t = jsonpath(data, '$..token')[0]
        token_type = jsonpath(data, '$..token_type')[0]
        # 空格拼接token
        t = " ".join([token_type, t])
        return t

    @property
    def member_id(self):
        data = login()
        m_id = jsonpath(data, '$..id')[0]
        return m_id

    @property
    def loan_id(self):
        """
        查询数据库，得到loan_id
        临时变量保存到Context当中
        return 返回loan标当中的id值
        """
        db = DBHandler()
        loan = db.query('SELECT * FROM laon WHERE STATUS=2 LIMIT 100;')
        # 关闭数据库连接
        db.close()
        return loan['id']




# def save_token():
#     data = login()
#     token = jsonpath(data, '$..token')[0]
#     token_type = jsonpath(data, '$..token_type')[0]
#     member_id = jsonpath(data, '$..id')[0]
#     # 空格拼接token
#     token = " ".join([token_type, token])
#
#     # return {"token": token, "memeber_id": member_id}
#     Context.token = token
#     Context.member_id = member_id
#
#     leave_amount = 0
#     Context.leave_amount = leave_amount
#     # 不需要返回值了


def replace_label(target):
    re_pattern = r"#(.*?)#"
    while re.findall(re_pattern, target):
        key = re.search(re_pattern, target).group(1)
        # value = getattr(CaseKeys, key, '')
        target = re.sub(re_pattern, str(getattr(Context, key)), target, 1)
    return target


if __name__ == '__main__':
    # 实例属性
    print(Context().token)
    print(Context().member_id)

# def save_loan_id():
#     """
#     查询数据库，得到loan_id
#     临时变量保存到Context当中
#     return 返回loan标当中的id值
#     """

# if __name__ == '__main__':
#     data = login()
# 麻烦
# token = data['data']['token_info']['token']
# token_type = data['data']['token_info']['token_type']


# jsonpath -> 专门用来解析json的路径工具
# jsonpath(data, '$..token')[0]
# jsonpath(data, '$..token_type')[0]
# jsonpath(data, '$..id')[0]
# data = save_token()
# print(data)
