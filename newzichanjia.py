# coding=utf-8

#from base import base
from testbase import base
import logger as log
import command as cmd

class zichanjia(base):

    def __init__(self, way,ip,port,apkname):
        base.__init__(self, way,ip,port,apkname)
        data = self.txttodic()
        type = cmd.adbgetpro(way,ip).lower()
        if data.has_key(type):
            self.dic = data[type]
        else:
            key = data.keys()
            log.info(key)
            self.dic = data[key[0]]

    def test_brows(self):
        #self.switch_con("NATIVE_APP")
        log.debug("进入欢迎页")
        self.sleep(5)
        width = self.size("width")
        log.info(width)
        height = self.size('height')
        log.info(height)
        self.swip(int(width) * 0.95, int(height) * 0.25, int(width) * 0.25, int(height) * 0.25)
        self.sleep(3)
        self.find_ele("id","com.xinhe99.zichanjia:id/btn_login")
        self.find_ele("id", "com.xinhe99.zichanjia:id/btn_login").click()
        self.sleep(2)

            #self.find_ele("id", "com.xinhe99.zichanjia:id/btn_login"):
            #self.find_ele("id", "com.djr.zichanjia:id/btn_login")
            #self.find_ele("id", "com.xinhe99.zichanjia:id/btn_login").click()
        #else:
           # pass
    def test_bottom(self):
        self.sleep(2)
        motou=self.find_ele("id","com.xinhe99.zichanjia:id/main_motou")
        motou.click()
        self.sleep(2)
        faxian=self.find_ele("id","com.xinhe99.zichanjia:id/main_zichanjia")
        faxian.click()
        self.sleep(2)
        wode=self.find_ele("id","com.xinhe99.zichanjia:id/main_me")
        wode.click()
        self.sleep(2)

    def test_login(self):
        '''self.sleep(1)
        self.find_ele('id',"com.xinhe99.zichanjia:id/negativeButton").click()
        self.sleep(1)
        self.find_ele('id',"com.xinhe99.zichanjia:id/negativeButton").click()
        '''
        self.sleep(1)
        log.debug("进入登陆页")
        self.find_ele("id", "com.xinhe99.zichanjia:id/main_me").click()
        self.sleep(3)
        #输入用户名
        username = self.find_ele("id", "com.xinhe99.zichanjia:id/login_name_et")
        username.send_keys(self.dic['username'])
        #输入密码
        userpsw = self.find_ele("id", "com.xinhe99.zichanjia:id/login_pwd_et")
        userpsw.send_keys(self.dic['userpwd'])
        #点击登录
        self.find_ele("id", "com.xinhe99.zichanjia:id/login_btn").click()
        self.sleep(3)
        #检查是否登录成功
        '''
        text=self.find_ele("id","com.djr.zichanjia:id/title").get_attribute("text")
        self.check_text("登录成功！",text.strip())
        self.find_ele("id", "com.djr.zichanjia:id/negativeButton").click()
        self.sleep(3)
        #忽略手势密码设置
        self.find_ele("name", "忽略").click()
        #没有实名认证，不认证直接返回
        #self.back()
        '''
    def test_sanbiao(self):
        self.wait_activity(".activity.MainActivity")

        log.debug("进入散标页")
        self.find_ele("id", "com.djr.zichanjia:id/main_bid").click()
        self.sleep(3)
        log.debug("选择项目状态")
        status = self.find_ele("id", "com.djr.zichanjia:id/tv_one")
        #print status.get_attribute('text')
        # status.__setattr__('text',u"投标中")
        # status.send_keys(u"投标中")
        # self.setvalue(status,u"投标中")
        '''
        if self.find_ele("id","com.djr.zichanjia:id/tv_null_xm"):
            log.info("没有散标可以投资")
        else:
            pass
        '''
        #查找可投资表
        lists=self.find_eles("id","com.djr.zichanjia:id/ll_weiwancheng")
        if len(lists) >0:
            for i in lists:
                blances=i.find_element_by_id("com.djr.zichanjia:id/tv_shengyu").get_attribute('text')
                log.info("剩余可投金额为:"+blances)
                log.info(blances)
                log.info(float(blances) > 0)
                if float(blances) > 0:
                    i.click()
                    #散标基本页单击立即投资
                    self.find_ele("id","com.djr.zichanjia:id/btn_fresh_invest").click()
                    self.sleep(2)
                    #散标详情页输入投资金额
                    log.info(self.dic['paymoney'])
                    self.find_ele("id", "com.djr.zichanjia:id/et_fresh_pay_money").click()
                    self.input(self.dic['paymoney'])
                    self.sleep(1)
                    #self.find_ele("id","com.djr.zichanjia:id/et_fresh_pay_money").send_keys(u'1000')
                    #单击下一步
                    self.find_ele("id","com.djr.zichanjia:id/btn_fresh_next").click()
                    self.sleep(2)
                    text = self.find_eles("classname", "android.widget.TextView")[0].get_attribute("text")

                    self.check_text("请确认您的购买信息", text.strip())
                    #单击确认投资
                    self.find_ele("id","com.djr.zichanjia:id/btn_commit").click()
                    self.sleep(3)
                    self.find_ele("id","com.djr.zichanjia:id/touzi_chakan").click()
                    break
                else:
                    continue
        else:
            log.error("没有可以投资的散标产品")



    def test_zichanbao(self):
        self.wait_activity(".activity.MainActivity")

        log.debug("进入资产包页")
        self.find_ele("id", "com.djr.zichanjia:id/main_zichanjia").click()
        self.sleep(3)
        #查找可投资表
        lists=self.find_eles("id","com.djr.zichanjia:id/ll_weiwancheng")
        if len(lists) >0:
            for i in lists:
                blances=i.find_element_by_id("com.djr.zichanjia:id/tv_shengyu").get_attribute('text')
                log.info("剩余可投金额为:"+blances)
                log.info(blances)
                log.info(float(blances) > 0)
                if float(blances) > 0:
                    i.click()
                    #散标基本页单击立即投资
                    self.find_ele("id","com.djr.zichanjia:id/btn_fresh_invest").click()
                    self.sleep(2)
                    #散标详情页输入投资金额
                    log.info(self.dic['paymoney'])
                    self.find_ele("id", "com.djr.zichanjia:id/et_fresh_pay_money").click()
                    self.input(self.dic['paymoney'])
                    self.sleep(1)
                    #self.find_ele("id","com.djr.zichanjia:id/et_fresh_pay_money").send_keys(u'1000')
                    #单击下一步
                    self.find_ele("id","com.djr.zichanjia:id/btn_fresh_next").click()
                    self.sleep(2)
                    text = self.find_eles("classname", "android.widget.TextView")[0].get_attribute("text")

                    self.check_text("请确认您的购买信息", text.strip())
                    #单击确认投资
                    self.find_ele("id","com.djr.zichanjia:id/btn_commit").click()
                    self.sleep(3)
                    self.find_ele("id","com.djr.zichanjia:id/touzi_chakan").click()
                    break
                else:
                    continue
        else:
            log.error("没有可以投资的资产包产品")



    def test_recharge(self):
        self.wait_activity(".activity.MainActivity")
        log.debug("进入个人中心页面")
        self.find_ele("id", "com.djr.zichanjia:id/main_me").click()
        self.sleep(3)
        total_m=self.find_ele("id","com.djr.zichanjia:id/tv_yue").get_attribute("text")
        #点击充值按钮
        self.find_ele("id","com.djr.zichanjia:id/btn_chongzhi").click()
        self.sleep(3)
        self.find_ele("id","com.djr.zichanjia:id/pay_bangding_bank_money").send_keys(self.dic['rechargemoney'])
        #单击前往富友充值按钮
        self.find_ele("id","com.djr.zichanjia:id/pay_bangding_bank_next").click()
        self.sleep(10)
        #edit_class=self.find_eles("classname","android.widget.EditText")
        #print len(edit_class)
        button_class=self.find_eles("calssname","android.widget.Button")
        #print len(button_class)
        #输入富友支付密码
        self.find_ele("classname", "android.widget.EditText[1]").send_keys(self.dic["fuyoupaypwd"])
        #edit_class[1].send_keys(self.dic["fuyoupaypwd"])
        #获取验证码
        self.find_ele("name", "获取验证码").click()
        #button_class[0].click()
        self.sleep(2)
        self.find_ele("name","确定").click()
        #输入验证码，为0000
        self.find_ele("classname", "android.widget.EditText[2]").send_keys(self.dic["fuyouyzm"])
        #edit_class[2].send_keys(self.dic["fuyouyzm"])
        #点击确认充值
        self.find_ele("name", "确认充值").click()
        #button_class[1].click()
        self.sleep(1)
        #充值确认框确定
        self.find_ele("name", "确定").click()
        self.sleep(10)
        #realtext=self.find_eles("classname","android.view.View")
        #text=realtext[1].get_attribute("name")
        #assert "恭喜您，您的操作已成功" == text
        self.check_text("恭喜您，您的操作已成功",self.find_eles("classname","android.view.View")[1].get_attribute("name"))
        #充值完成确定
        self.find_ele("name", "确定").click()
        #print total_m.replace(',', '')
        realtotal=self.find_ele("id","com.djr.zichanjia:id/tv_yue").get_attribute("text")
        #print realtotal.replace(',', '')
        total=float(total_m.replace(',', ''))+float(self.dic['rechargemoney'])
        self.check_text(str('%.2f' % total),realtotal.replace(',', '') )
        '''
        else:
            self.find_ele("name", "确定").click()
            log.error("充值失败，失败信息为："+realtext[1].get_attribute("name"))
            self.sleep(3)
        '''

    def test_withdraw(self):
        self.wait_activity(".activity.MainActivity")
        log.debug("进入个人中心页面")
        self.find_ele("id", "com.djr.zichanjia:id/main_me").click()
        self.sleep(3)
        total_m = self.find_ele("id", "com.djr.zichanjia:id/tv_yue").get_attribute("text")
        # 点击提现按钮
        self.find_ele("id", "com.djr.zichanjia:id/btn_tixian").click()
        self.sleep(3)
        self.find_ele("id", "com.djr.zichanjia:id/drawmoney_et_money").send_keys(self.dic['withdrawmoney'])
        # 单击前往富友充值按钮
        self.find_ele("id", "com.djr.zichanjia:id/drawmoney_btn_next").click()
        self.sleep(10)
        #edit_class = self.find_eles("classname", "android.widget.EditText")
        #print len(edit_class)
        # 输入富友支付密码
        self.find_ele("classname", "android.widget.EditText[0]").send_keys(self.dic["fuyoupaypwd"])
        #edit_class[0].send_keys(self.dic["fuyoupaypwd"])
        # 获取验证码
        self.find_ele("name", "获取验证码").click()
        self.sleep(2)
        self.find_ele("name", "确定").click()
        # 输入验证码，为0000
        self.find_ele("classname", "android.widget.EditText[1]").send_keys(self.dic["fuyouyzm"])
        #edit_class[1].send_keys(self.dic["fuyouyzm"])
        # 点击确认提现
        self.find_ele("name", "确认").click()
        self.sleep(2)
        # 提现确认框确定
        self.find_ele("name", "确定").click()
        self.sleep(2)
        #realtext = self.find_eles("classname", "android.view.View")
        '''
        print len(realtext)
        for i in range(len(realtext)):
            print realtext[i].get_attribute("name")
        '''
        self.check_text("恭喜您，您的操作已成功", self.find_eles("classname", "android.view.View")[1].get_attribute("name"))
        # 提现完成确定
        self.find_ele("name", "确定").click()
        #print total_m.replace(',', '')
        realtotal = self.find_ele("id", "com.djr.zichanjia:id/tv_yue").get_attribute("text")
        #print realtotal.replace(',', '')
        total = float(total_m.replace(',', '')) - float(self.dic['withdrawmoney'])
        self.check_text(str(total),realtotal.replace(',', ''))
        # 初始化页面，进行返回
        '''
        else:
            log.error("提现失败，失败信息为：" + realtext[1].get_attribute("name"))
            self.find_ele("name", "确定").click()
            self.sleep(3)
        '''
    def test_logout(self):
        width = self.size("width")
        log.info(width)
        height = self.size('height')
        log.info(height)
        #self.wait_activity(".activity.MainActivity")
        self.find_ele("id", "com.xinhe99.zichanjia:id/main_me").click()
        self.sleep(3)
        self.swip(int(width) * 0.5, 1129, int(width) * 0.5, 300)
        self.sleep(3)
        # self.find_ele("id","com.djr.zichanjia:id/negativeButton").click()
        self.sleep(1)
        self.find_ele("id", "com.xinhe99.zichanjia:id/rl_setting").click()
        self.sleep(3)
        self.swip(int(width) * 0.5, int(height) * 0.95, int(width) * 0.5, int(height) * 0.25)
        self.sleep(3)
        self.find_ele("id", "com.xinhe99.zichanjia:id/but_finish").click()  # 安全退出
        self.sleep(3)
        self.find_ele("name", "确定").click()
        self.sleep(3)


