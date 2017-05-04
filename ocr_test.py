# coding=utf-8
import command as cmd
import newzichanjia
import logger as log
import unittest
import HTMLTestRunner
import time
import sys
import ocr
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

class ocrtest(unittest.TestCase):

    def setUp(self):
        self.ip = ip
        self.port = port
        self.apkname = apkname
        self.way=way
        self.test = ocr.ocr(self.way,self.ip,self.port,self.apkname)

    def test_welcome(self):
        log.debug("欢迎页")
        self.test.stat_appium()
        self.test.test_brows()


    def test_login(self):
        log.debug("开始登录")
        self.test.test_login()


    def test_xinjie_zixun(self):
        self.test.xinjie_zixun()

    def test_xinjie_bulu(self):
        self.test.xinjie_bulu()

    @unittest.skip('暂时跳过')
    def test_torecharge(self):
        log.debug("开始充值")
        self.test.test_recharge()

    @unittest.skip('暂时跳过')
    def test_towithdraw(self):
        log.debug("开始提现")
        self.test.test_withdraw()

    @unittest.skip('暂时跳过')
    def test_tosanbiao(self):
        log.debug("开始投资")
        self.test.test_sanbiao()

    @unittest.skip('暂时跳过')
    def test_tozichanbao(self):
        log.debug("开始投资")
        self.test.test_zichanbao()

    @unittest.skip('暂时跳过')
    def test_tologout(self):
        log.debug("开始退出")
        self.test.test_logout()

    def tearDown(self):
        pass


def run(ip):
    print "脚本执行"
    testsuite = unittest.TestSuite()
    testsuite.addTest(ocrtest("test_welcome"))
    testsuite.addTest(ocrtest("test_login"))
    testsuite.addTest(ocrtest("test_xinjie_zixun"))
    testsuite.addTest(ocrtest("test_xinjie_bulu"))
    testsuite.addTest(ocrtest("test_torecharge"))
    testsuite.addTest(ocrtest("test_tosanbiao"))
    testsuite.addTest(ocrtest("test_tozichanbao"))
    testsuite.addTest(ocrtest("test_towithdraw"))
    testsuite.addTest(ocrtest("test_tologout"))
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


