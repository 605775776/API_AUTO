# import yaml
#
# # 写成类 不如写成方法
#
#
# class YamlHandler:
#
#     def __init__(self, file, encoding='utf-8'):
#         self.file = file
#         self.encoding = encoding
#
#     def read_yaml(self):
#         with open(self.file) as f:
#             return yaml.load(f.read(), Loader=yaml.FullLoader)
#
#     def write_yaml(self, data):
#         with open(self.file, mode='w') as f:
#             yaml.dump(data, stream=f, allow_unicode=True)

# if __name__ == '__main__':
#     a = YamlHandler('config.yaml').read_yaml()
#     YamlHandler('config2.yaml').write_yaml(a)
