# coding=utf-8
import logger as log
import command as cmd
import time
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)
driver=None
class base():
    #global driver
    '''
    def __init__(self, driver, ip):
        self.driver = driver
        self.ip = ip
    '''

    def __init__(self,way,ip,port,apkname):
        self.way=way
        self.ip=ip
        self.port=port
        self.apkname=apkname
        #self.packageName = packageName
        #driver = stat_appium
        #log.error(driver)

    def stat_appium(self):
        global driver
        desired_caps = {}
        desired_caps['device'] = 'android'
        desired_caps['platformName'] = 'Android'  # 测试平台
        desired_caps['browserName'] = ''
        desired_caps['version'] = cmd.adbgetversion(self.way,self.ip) # 系统版本
        if cmd.checkip(self.ip):
            desired_caps['deviceName'] = self.ip+':'+str(5555)  # 模拟器名称或者是真机型号
            desired_caps['udid'] = self.ip+':'+str(5555)
        else:
            desired_caps['deviceName'] = self.ip  # 模拟器名称或者是真机型号
            desired_caps['udid'] = self.ip
        desired_caps['resetKeyboard'] = 'True'
        desired_caps['unicodeKeyboard'] = 'True'
        desired_caps['app'] = cmd.file_path+"\\" + self.apkname
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        #资产家测试必须有appwaitactivity
        #desired_caps['appWaitActivity'] = '.activity.WelcomeActivity'
        # 如果知道被测试对象的apppage，appActivity可以加上下面这两个参数，如果不知道，可以注释掉，不影响用例执行
        #desired_caps['appPackage'] = 'com.djr.zichanjia'  # 要测试的app
        #desired_caps['appActivity'] = '.activity.WelcomeActivity'  # 当前活动应用

        driver= webdriver.Remote('http://127.0.0.1:' + str(self.port) + '/wd/hub', desired_caps)
        log.info(driver)

        #star=driver.find_element_by_id(id).location
        #return driver
    #driver=stat_appium
    #driver=stat_appium()

    def txttodic(self):
        filename="\\data.txt"
        return cmd.texttodic(filename)

    def screenshot(self, text):
        log.debug("开始截屏")
        tm = time.strftime('%H-%M-%S', time.localtime(time.time()))
        driver.get_screenshot_as_file(cmd.img_path + "\\" + self.ip + "-" + tm + "-" + text + ".png")

    def find_ele(self, *loc):
        log.debug("查找元素")
        len(loc)
        log.info(loc[0])
        log.info(loc[1])
        try:
            el = ""
            if loc[0] == "id":
                el = driver.find_element_by_id(loc[1])
            elif loc[0] == "name":
                el = driver.find_element_by_name(loc[1])
            elif loc[0] == "xpath":
                el = driver.find_element_by_xpath(loc[1])
            elif loc[0] == "classname":
                el = driver.find_element_by_class_name(loc[1])
            elif loc[0] == "accessibilityid":
                el = driver.find_element_by_accessibility_id(loc[1])
            log.info(el)
            return el
        except Exception as e:
            log.error(e)
            log.error("设备" + self.ip + "中，元素" + loc[1] + "不存在")
            self.screenshot("element-err")

    def find_eles(self, *loc):
        log.debug("查找同属性的元素")
        len(loc)
        log.info(loc[0])
        log.info(loc[1])
        try:
            el = ""
            if loc[0] == "id":
                el = driver.find_elements_by_id(loc[1])
            elif loc[0] == "name":
                el = driver.find_elements_by_name(loc[1])
            elif loc[0] == "xpath":
                el = driver.find_elements_by_xpath(loc[1])
            elif loc[0] == "classname":
                el = driver.find_elements_by_class_name(loc[1])
            log.info(el)
            return el
        except Exception as e:
            log.error(e)
            log.error("设备" + self.ip + "中，元素" + loc[1] + "不存在")
            self.screenshot("element-err")

    def iselementexist(self, *loc):
        log.debug("判断元素是否存在")
        try:
            el = ""
            if loc[0] == "id":
                el = driver.find_element_by_id(loc[1])
            elif loc[0] == "name":
                el = driver.find_element_by_name(loc[1])
            elif loc[0] == "xpath":
                el = driver.find_element_by_xpath(loc[1])
            elif loc[0] == "classname":
                el = driver.find_element_by_class_name(loc[1])
            log.info(el)
            log.info(loc[1]+"元素存在")
            return True
        except Exception:
            log.info(loc[1]+"元素不存在")
            return False

    def check_text(self, value, realtext):
        log.debug("检查文本")
        try:
            assert realtext == value,"设备" + self.ip + "中，预期文字是：" + value + "，实际文字是：" + realtext
            log.info("文字校验通过")
        except AssertionError,  e:
            self.screenshot("text-err")
            log.error(e)
            #raise e


    def size(self, value):
        # driver.Remote.get_window_size()
        return driver.get_window_size()[value]

    def swip(self,x1,y1,x2,y2):
        log.debug("进行滑屏")
        try:
            driver.swipe(x1,y1,x2,y2, 1000)
        except Exception as e:
            log.error(e)
            log.error("设备" + self.ip + "滑动失败")
            self.screenshot("swipe-err")

    def swipcontrol(self,*loc):
        log.debug("控件滑动")
        try:
            start=self.find_ele(*loc).location
            print start
            width = self.size("width")
            log.info(width)
            height = self.size('height')
            log.info(height)
            driver.swipe(int(width) * 0.95, int(height) * 0.25, int(width) * 0.25, int(height) * 0.25, 1000)
        except Exception as e:
            log.error(e)
            log.error("设备" + self.ip + "滑动失败")
            self.screenshot("swipe-err")

    def input(self,value):
        if "." in value:
            val = value.split(".")[0]
        else:
            val = value
        for i in val:
            cmd.adbinput(self.way,self.ip,int(i))

    def switch_con(self, con):
        driver.switch_to.context(con)

    def sleep(self, sec):
        time.sleep(sec)

    def back(self):
        driver.press_keycode("4")

    def setvalue(self, element, value):
        driver.set_value(element, value)

    def con(self):
        return driver.contexts

    def getH5(self):
        return driver.contexts[-1]

    def quit(self):
        driver.quit()

    def wait_activity(self, activity):
        log.debug("activity检查")
        #log.error(activity)
        for i in range(4):
            log.info("当前activity是")
            log.info(driver.current_activity)
            if driver.current_activity == activity or driver.current_activity == None:
                break
            else:
                driver.back()
                #cmd.adbback(self.ip)

    def appWaitActivity(self,activity,timeout):
        WebDriverWait(driver,timeout).until(lambda d: d.current_activity == activity)

    def touchaction(self,el,x,y):
        TouchAction(driver).move_to(el,x,y).perform()



