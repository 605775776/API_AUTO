from common.logger_handler import logger


def main():
    print("hello")
    logger.info("msg")


def hello():
    logger.error("error")


if __name__ == '__main__':
    main()
