import os

class Config:

    # 项目路径
    root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # config路径
    config_path = os.path.join(root_path, 'config')

    # 日志配置路径
    #logger_setting_path = os.path.join(root_path, 'config/config.yaml')
    yaml_config_path = os.path.join(config_path, 'config.yaml')

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