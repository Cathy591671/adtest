# coding=utf-8
import command as cmd
import newzichanjia
import logger as log
import unittest
import HTMLTestRunner
import time
import sys
import jinkuihua
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
global ip
global port
global apkname
#global packagename
#global activity
ip = None
port = None
apkname = None
way=None
#packagename = None

class jkhtest(unittest.TestCase):

    def setUp(self):
        self.ip = ip
        self.port = port
        self.apkname = apkname
        self.way=way
        self.test = jinkuihua.jinkuihua(self.way,self.ip,self.port,self.apkname)

    def test_welcome(self):
        log.debug("欢迎页")
        self.test.stat_appium()
        self.test.test_brows()

    def test_login(self):
        log.debug("登录")
        self.test.test_login()




    def tearDown(self):
        pass


def run(ip):
    print "脚本执行"
    testsuite = unittest.TestSuite()
    testsuite.addTest(jkhtest("test_welcome"))
    testsuite.addTest(jkhtest("test_login"))

    # 确定生成报告的路径
    tm = time.strftime('%d-%H-%M-%S', time.localtime(time.time()))
    #filePath = "D:\python\\file\pyResult.html"
    filePath = cmd.log_path+"/"+ip+"-pyResult.html"
    fp = file(filePath, 'wb')

    #a = MyTestCase()

    # 生成报告的Title,描述
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='这是设备'+ip+'的测试报告')
    runner.run(testsuite)

'''if __name__ == '__main__':
    ip='10.167.170.46'
    port='4723'
    apkname='android_176_1114_9.apk'
    run(ip)'''


