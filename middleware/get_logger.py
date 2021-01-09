from common.logger_handler import LoggerHandler
from middleware.yaml_handler import yaml_data


class Mylogger(LoggerHandler):

    def __init__(self):
        super().__init__(name=yaml_data['logger']['name'],
                         level=yaml_data['logger']['level'],
                         file=yaml_data['logger']['file'])


logger = Mylogger()

# if __name__ == '__main__':
#     print(logger)