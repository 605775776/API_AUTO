import random
import yaml
from common.request_handler import RequestsHandler
from config.setting import Config

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















