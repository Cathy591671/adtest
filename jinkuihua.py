# coding=utf-8

#from base import base
from testbase import base
import logger as log
import command as cmd

class jinkuihua(base):

    def __init__(self, way,ip,port,apkname):
        base.__init__(self, way,ip,port,apkname)
        data = self.txttodic()
        print "data"
        print data
        type = cmd.adbgetpro(way,ip).lower()
        if data.has_key(type):
            self.dic = data[type]
        else:
            key = data.keys()
            log.info(key)
            self.dic = data[key[0]]

    def test_brows(self):
        #self.switch_con("NATIVE_APP")
        width = self.size("width")
        height = self.size('height')
        log.debug("进入欢迎页")
        self.sleep(4)
        self.swip(int(width) * 0.95, int(height) * 0.25, int(width) * 0.25, int(height) * 0.25)
        self.sleep(2)
        self.swip(int(width) * 0.95, int(height) * 0.25, int(width) * 0.25, int(height) * 0.25)
        self.sleep(2)
        self.swip(int(width) * 0.5, int(height) * 0.95, int(width) * 0.5, int(height) * 0.95)
        self.sleep(2)
        self.swip(int(width) * 0.5, int(height) * 0.5, int(width) * 0.5, int(height) * 0.5)
        self.sleep(1)
        self.find_ele("id","com.cgs.fund:id/user").click()
        self.sleep(1)

    def test_login(self):
        self.sleep(1)
        username=self.find_ele("id","com.cgs.fund:id/acount")
        username.send_keys(self.dic['username'])
        password=self.find_ele("id","com.cgs.fund:id/pwd")
        password.send_keys(self.dic['password'])
        self.find_ele("id","com.cgs.fund:id/login").click()
        self.sleep(2)







