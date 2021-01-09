from common.db_handler import DBHandler
from middleware.yaml_handler import yaml_data


class MyDBHandler(DBHandler):
    def __init__(self):
        super().__init__(host=yaml_data['database']['host'],
                         port=yaml_data['database']['port'],
                         user=yaml_data['database']['user'],
                         password=yaml_data['database']['password'],
                         charset=yaml_data['database']['charset'],
                         database=yaml_data['database']['database'])
