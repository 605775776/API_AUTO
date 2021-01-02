# 写成类模块
import os
class LoggerConfig:

    logger_name = 'python25'
    logger_file = 'python251111111.txt'
    level = 'DEBUG'

class Config:

    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # 测试数据路径
    data_path = os.path.join(root_path, 'data\\test_cases.xlsx')

    # 测试用例路径
    case_path = os.path.join(root_path, 'test_cases')

    # 测试报告路径
    report_path = os.path.join(root_path, 'report')
    if not os.path.exists(report_path):
        os.mkdir(report_path)

class DevConfig(Config):

    # 项目的域名
    host = 'http://120.78.128.25:8766/futureloan'

# if __name__ == '__main__':
    # print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    # root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    #
    # print(os.path.join(root_path, 'data\cases.xlsx'))