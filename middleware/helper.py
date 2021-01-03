import random
import yaml
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


    def save_token():
        res = login()
        token = jsonpath(data, '$..token')[0]
        token_type = jsonpath(data, '$..token_type')[0]
        member_id = jsonpath(data, '$..id')[0]

if __name__ == '__main__':
    data = login()
    pass
    # 麻烦
    # token = data['data']['token_info']['token']
    # token_type = data['data']['token_info']['token_type']


    # jsonpath -> 专门用来解析json的路径工具
    # jsonpath(data, '$..token')[0]
    # jsonpath(data, '$..token_type')[0]
    # jsonpath(data, '$..id')[0]














