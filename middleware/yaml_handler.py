import yaml
from config.setting import Config


class YamlHandler:

    def __init__(self, file, encoding='utf-8'):
        self.file = file
        self.encoding = encoding

    def read_yaml(self):
        with open(self.file) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            f.close()
            return data

    def write_yaml(self, data):
        with open(self.file, mode='w') as f:
            yaml.dump(data, stream=f, allow_unicode=True)


# 读取本项目当中的yaml所有配置项

yaml_data = YamlHandler(Config.yaml_config_path).read_yaml()
