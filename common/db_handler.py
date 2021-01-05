import pymysql
from pymysql.cursors import DictCursor


class DBHandler:

    def __init__(self,
                 host,
                 port,
                 user,
                 password,
                 charset,
                 database,
                 cursorclass=DictCursor,
                 **kw):
        self.conn = pymysql.connect(host=host,
                                    port=port,
                                    user=user,
                                    password=password,
                                    charset=charset,
                                    database=database,
                                    cursorclass=cursorclass,
                                    **kw)
        self.cursor = self.conn.cursor()

    def query(self, sql, args=None, one=True):
        self.cursor.execute(sql, args)
        # 提交 否则要重新初始化游标对象
        self.conn.commit()
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':

    from config.setting import Config
    import yaml
    f = open(Config.yaml_config_path, encoding='utf-8')
    yaml_data = yaml.load(f, Loader=yaml.FullLoader)
    # print(yaml_data)

    db = DBHandler(host=yaml_data['database']['host'],
                   port=yaml_data['database']['port'],
                   user=yaml_data['database']['user'],
                   password=yaml_data['database']['password'],
                   charset=yaml_data['database']['charset'],
                   database=yaml_data['database']['database']
                   )

    res = db.query("select * from crm_resource where id = 1")
    print(res)
