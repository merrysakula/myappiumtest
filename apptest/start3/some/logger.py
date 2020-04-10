#coding=utf-8
# import logging
# logging.basicConfig(level = logging.INFO,format='%(asctime)s - %(name)s -%(levelname)s -%(message)s')
# logger = logging.getLogger(__name__)
# logger.info('hh')

#设置logging 创建一个FileHandler 对输出消息格式设置 添加到logger 将日志写入指定文件
import logging
from logging.handlers import RotatingFileHandler#日志回滚
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
#定义一个RotatingFileHandler最多3个日志文件，每个日志文件最大1k
rHandler = RotatingFileHandler('log.txt',maxBytes=1*1024,backupCount=3)
rHandler.setLevel(logging.INFO)
# handler = logging.FileHandler('log.txt')
# handler.setLevel(logging.INFO)
# formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s -%(message)s')
# handler.setFormatter(formatter)
#logger添加StreamHandler将日志输出屏幕
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logger.addHandler(rHandler)
logger.addHandler(console)
# logger.addHandler(handler)
logger.warning('hh')
