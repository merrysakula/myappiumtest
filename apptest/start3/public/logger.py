#coding=utf-8
import logging,os,time
mypath = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
logpath = mypath('../logs')
class logger:
    def __init__(self):
        filename =''.join(time.strftime('%Y%m%d'))+''.join('.log')
        self.logname = os.path.join(logpath,filename)
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.format = logging.Formatter('[%(asctime)s]-[%(levelname)s]-%(message)s')
    def output(self,level,message):
        fh = logging.FileHandler(self.logname,'a')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(self.format)
        self.logger.addHandler(fh)
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)
        ch.setFormatter(self.format)
        self.logger.addHandler(ch)
        if level == 'info':
            self.logger.info(message)
        elif level == 'debug':
            self.logger.debug(message)
        elif level == 'warning':
            self.logger.warning(message)
        elif level == 'error':
            self.logger.error(message)
            #防止重复打印
        self.logger.removeHandler(fh)
        self.logger.removeHandler(ch)
    def info(self,message):
        self.output('info', message)
    def debug(self,message):
        self.output('debug', message)
    def warn(self,message):
        self.output('warn', message)
    def error(self,message):
        self.output('error', message)
if __name__ == '__main__':
    log = logger()
    log.info('hhh')
