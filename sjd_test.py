# coding=utf-8
import command as cmd
import shoujidai
import logger as log
import unittest
import HTMLTestRunner
import time
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
global ip
global port
global apkname
#global packagename
#global activity
way=None
ip = None
port = None
apkname = None
#packagename = None

class appiumtest(unittest.TestCase):

    def setUp(self):
        self.way=way
        self.ip = ip
        self.port = port
        self.apkname = apkname
        self.test = shoujidai.shoujidai(self.way,self.ip, self.port,self.apkname)


    #@unittest.skip('暂时跳过')
    def test_toregister(self):
        self.test.stat_appium()
        log.debug("开始注册")
        self.test.test_regist()

    def test_tologin(self):
        log.debug("滑动")
        self.test.test_brows()
        log.debug("开始登陆")
        self.test.test_login()

    # @unittest.skip('暂时跳过')
    def test_toidentityauth(self):
        log.debug("开始查看身份信息")
        self.test.test_identityauth()

    #@unittest.skip('暂时跳过')
    def test_tocontactauth(self):
        log.debug("开始添加紧急联系人")
        self.test.test_contactauth()

    #@unittest.skip('暂时跳过')
    def test_tomoreauth(self):
        log.debug("开始添加更多信息")
        self.test.test_moreauth()

    #@unittest.skip('暂时跳过')
    def test_tobankcard(self):
        log.debug("开始绑定银行卡")
        self.test.test_bankcard()

    @unittest.skip('暂时跳过')
    def test_toborrow(self):
        log.debug("开始借款")
        self.test.test_borrow()

    @unittest.skip('暂时跳过')
    def test_tonormalrefund(self):
        log.debug("开始正常还款")
        self.test.test_normalrefund()

    @unittest.skip('暂时跳过')
    def test_toadvancerefund(self):
        log.debug("开始提前还款")
        self.test.test_advancerefund()

    #@unittest.skip('暂时跳过')
    def test_toloaninfo(self):
        log.debug("查询借款记录")
        self.test.test_loaninfo()

    #@unittest.skip('暂时跳过')
    def test_todiscount(self):
        log.debug("开始查询优惠券")
        self.test.test_discount()

    #@unittest.skip('暂时跳过')
    def test_tologout(self):
        log.debug("开始退出")
        self.test.test_logout()

    def tearDown(self):
        pass
        #self.test.quit()

def run(ip):
    print "脚本执行"
    testsuite = unittest.TestSuite()
    testsuite.addTest(appiumtest("test_toregister"))
    testsuite.addTest(appiumtest("test_tologin"))
    testsuite.addTest(appiumtest("test_toidentityauth"))
    testsuite.addTest(appiumtest("test_tocontactauth"))
    testsuite.addTest(appiumtest("test_tomoreauth"))
    testsuite.addTest(appiumtest("test_tobankcard"))
    testsuite.addTest(appiumtest("test_toborrow"))
    testsuite.addTest(appiumtest("test_tonormalrefund"))
    testsuite.addTest(appiumtest("test_toadvancerefund"))
    testsuite.addTest(appiumtest("test_toloaninfo"))
    testsuite.addTest(appiumtest("test_todiscount"))
    testsuite.addTest(appiumtest("test_tologout"))
    # 确定生成报告的路径
    tm = time.strftime('%d-%H-%M-%S', time.localtime(time.time()))
    #filePath = "D:\python\\file\pyResult.html"
    filePath = cmd.log_path+"/"+ip+tm+"-pyResult.html"
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


