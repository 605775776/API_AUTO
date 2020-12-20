import logging


class LoggerHandler():

    def __init__(self,
                 name='admin',
                 level='DEBUG',
                 file=None,
                 format='%(filename)s-%(lineno)d-%(name)s-%(levelname)s-%(message)s'):

        logger = logging.getLogger(name)
        # 设置级别
        logger.setLevel(level)

        # 初始化format
        fmt = logging.Formatter(format)

        # 初始化处理器filename
        if file:
            file_handler = logging.FileHandler()
            # 设置handler的级别
            file_handler.setLevel('DEBUG')
            # 设置日志格式
            file_handler.setFormatter(fmt)
            # 添加handler
            logger.addHandler(file_handler)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel('DEBUG')
        stream_handler.setFormatter(fmt)
        logger.addHandler(stream_handler)
        self.logger = logger

    def debug(self, msg):
        return self.logger.debug(msg)

    def info(self, msg):
        return self.logger.info(msg)
    def warning(self, msg):
        return self.logger.warning(msg)
    def error(self, msg):
        return self.logger.error(msg)
    def critical(self, msg):
        return self.logger.critical(msg)

if __name__ == '__main__':
    logger = LoggerHandler()
    logger.debug('hello')



