#/usr/bin/env python
import logging

def WriteLog():
    log_name = "test"
    log_filename = "/tmp/test.log"
    log_level = logging.DEBUG
    format = logging.Formatter('[%(asctime)s] [%(process)d] [%(thread)d] [%(filename)10s] [line:%(lineno)4d] [%(levelname)-6s] %(message)s')
    handler = logging.handlers.RotatingFileHandler(log_filename, mode='a', maxBytes=10*1024*1024, backupCount=5)
    handler.setFormatter(format)
    logger = logging.getLogger(log_name)
    logger.addHandler(handler)
    logger.setLevel(log_level)
    return logger
    

if __name__ == "__main__":
    WriteLog().info('123')  #等价下面两行
    # writelog = WriteLog()
    # writelog.info('123')

