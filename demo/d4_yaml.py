import yaml

# 读取 加载配置项
# f = open("demo_config.yaml")
# data = yaml.load(f.read(), Loader=yaml.FullLoader)
#
# print(data)
#
# f.closed()
def read_yaml(file, encoding='utf-8'):
    with open(file, encoding=encoding) as f:
        return yaml.load(f.read(), Loader=yaml.FullLoader)
