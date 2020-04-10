#coding=utf-8
import os,platform,random,time
from start3.public.logger import logger
from start3.public.getdevice import devices
log = logger()
dev = devices().getdevicename()
class appium:
    def __init__(self,device):
        self.device = device
    def _start_appium(self,aport,bpport):
        #清理logcat与appium所有进程
        if platform.system() == 'Windows':
            import subprocess
            subprocess.Popen('appium -p %s -bp %s -U %s'%(aport,bpport,self.device),shell=True)
    def start_appium(self):
        '''
                        动appium
        p:appium port
        bp:bootstrap port
        :return: 返回appium端口参数
        '''
        aport = random.randint(4700,4900)
        bpport = random.randint(4700,4900)
        self._start_appium(aport, bpport)
        log.info('appium -p %s -bp %s -U %s'%(aport,bpport,self.device))
        time.sleep(5)
        return aport
    def stop_appium(self):
        if platform == 'Windows':
            os.popen('taskkill /f /im node.exe')
if __name__ == '__main__':
    s = appium(dev)
    s.start_appium()