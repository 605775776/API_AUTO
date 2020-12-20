import logging

# logging.info("info")
# logging.debug("debug")
# logging.warning("waring")
# logging.error("error")
# logging.critical("critical")

# 初始化logger 收集器
logger = logging.getLogger("python25")
# 设置级别 高于debug级别才打印 笔记本
logger.setLevel('DEBUG')

# 笔的默认级别是warning 默认是使用控制台输出
# 放到一个file文件当中
handler = logging.FileHandler('log.txt')

# 控制台输出日志级别
console_handler = logging.StreamHandler()

handler.setLevel('DEBUG')

# 添加handler
logger.addHandler(handler)

# handler 设置格式
fmt = logging.Formatter('%(filename)s-%(lineno)d-%(name)s-%(levelname)s-%(message)s')
handler.setFormatter(fmt)




logger.info('hello')
logger.info('hello')

