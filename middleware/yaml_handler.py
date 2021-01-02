import yaml
class YamlHandler:

    def __init__(self, file, encoding='utf-8'):
        self.file = file
        self.encoding = encoding

    def read_yaml(self):
        with open(self.file) as f:
            return yaml.load(f, Loader=yaml.FullLoader)