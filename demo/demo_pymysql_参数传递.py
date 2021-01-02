"""
python 操作数据库
mysql oracle sqlserver mongodb access
"""
import pymysql

from pymysql.cursors import DictCursor

# 建立连接
conn = pymysql.connect(host='120.78.128.25',
                       port=3306,
                       user="future",
                       password="123456",
                       charset="utf8",
                       database='futureloan',
                       cursorclass=DictCursor)

# 游标
cursor = conn.cursor()

# 发起请求 执行sql语句 第一种方法传递参数 不要用format sql注入
mobile = "15710533996"
# cursor.execute('select * from member where mobile_phone={};'.format(mobile))
# 2：args 参数 %s 占位符 args = 列表，或者元组
cursor.execute('select * from member where mobile_phone=%s;', args=[mobile])


# 获取游标结果 会影响
res_all = cursor.fetchall()
res_one = cursor.fetchone()

# 关闭
cursor.close()
conn.close()