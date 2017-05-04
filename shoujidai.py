# coding=utf-8

#from base import base
from testbase import base
import logger as log
import random
import command as cmd
import interface
import mysqlexe

relation=('配偶','直系亲属','同事','朋友')
education=('本科以上','大专','高中','高中以下')
marriage=('未婚','已婚','离异','其他')

class shoujidai(base):
    def __init__(self, way,ip,port,apkname):
        base.__init__(self, way,ip,port,apkname)
        data = self.txttodic()
        log.info(data)
        self.mysql=mysqlexe.mysql()
        type = cmd.adbgetpro(way,ip).lower()
        if data is not None:
            if data.has_key(type):
                self.dic = data[type]
            else:
                key = data.keys()
                log.info(key)
                self.dic = data[key[0]]

    def test_regist(self):
        log.debug("使用接口进行注册并个人信息认证")
        interface.check(self.dic['username'],self.dic['userpwd'])

    def test_brows(self):
        #self.switch_con("NATIVE_APP")
        log.debug("进入欢迎页")
        self.sleep(3)
        width = self.size("width")
        log.info(width)
        height = self.size('height')
        log.info(height)
        self.swip(int(width) * 0.95, int(height) * 0.25, int(width) * 0.25, int(height) * 0.25)
        self.swip(int(width) * 0.95, int(height) * 0.25, int(width) * 0.25, int(height) * 0.25)
        self.swip(int(width) * 0.95, int(height) * 0.25, int(width) * 0.25, int(height) * 0.25)
        self.swip(int(width) * 0.95, int(height) * 0.25, int(width) * 0.25, int(height) * 0.25)
        self.sleep(3)
        self.find_ele("classname", "android.widget.ImageView").click()
        self.sleep(2)

    def test_login(self):
        self.wait_activity(".ui.activity.HomeActivity")
        log.debug("进入登陆页")
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_homeme").click()
        self.sleep(3)
        #输入用户名
        username = self.find_ele("id", "com.xihe.moblie.credit:id/et_account")
        username.send_keys(self.dic['username'])
        #输入密码
        userpsw = self.find_ele("id", "com.xihe.moblie.credit:id/et_password")
        userpsw.send_keys(self.dic['userpwd'])
        #点击登录
        self.find_ele("id", "com.xihe.moblie.credit:id/btn_send_data").click()
        self.sleep(1)

    def test_identityauth(self):
        self.wait_activity(".ui.activity.HomeActivity")
        log.debug("进入个人中心页面")
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_homeme").click()
        self.sleep(3)
        # 单击个人信息
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_user_info").click()
        # 单击身份认证信息
        contact = self.find_ele("id", "com.xihe.moblie.credit:id/user_info_card").get_attribute("text")
        if contact == '去完善':
            log.error("个人身份信息未完善，请完善")
        else:
            #查看身份信息
            self.find_ele("id", "com.xihe.moblie.credit:id/user_info_card").click()
            self.find_ele("id", "com.xihe.moblie.credit:id/card_person").click()
            self.sleep(1)
            self.find_ele("id", "com.xihe.moblie.credit:id/head_back").click()
            self.find_ele("id", "com.xihe.moblie.credit:id/card_on").click()
            self.sleep(1)
            self.find_ele("id", "com.xihe.moblie.credit:id/head_back").click()
            self.find_ele("id", "com.xihe.moblie.credit:id/card_off").click()
            self.sleep(1)
            self.find_ele("id", "com.xihe.moblie.credit:id/head_back").click()
            self.find_ele("id", "com.xihe.moblie.credit:id/head_back").click()
        # 单击返回到个人信息页面
        self.find_ele("id", "com.xihe.moblie.credit:id/head_back").click()

    def test_contactauth(self):
        self.wait_activity(".ui.activity.HomeActivity")
        log.debug("进入个人中心页面")
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_homeme").click()
        self.sleep(3)
        #单击个人信息
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_user_info").click()
        contact=self.find_ele("id", "com.xihe.moblie.credit:id/tv_user_info_connecter").get_attribute("text")
        if contact=='去完善':
            self.find_ele("id", "com.xihe.moblie.credit:id/user_info_connecter").click()
            #进行添加紧急联系人1信息
            self.find_ele("id", "com.xihe.moblie.credit:id/add1").click()
            self.sleep(1)
            self.find_ele("id", "com.xihe.moblie.credit:id/relationshap_item").click()
            self.find_ele("name",random.choice(relation)).click()
            self.find_ele("id", "com.xihe.moblie.credit:id/pickConnecter").click()
            #xpath1="//android.widget.RelativeLayout[contains(@resource-id,'com.android.contacts:id/contacts_body')]//android.widget.ListView[contains(@resource-id,'com.android.contacts:id/main_list')]//android.view.View[1]//android.widget.FrameLayout[contains(@resource-id,'com.android.contacts:id/contact_list_item')]"
            #log.info(self.find_eles("id", 'com.android.contacts:id/name'))
            self.find_ele("xpath", "//android.widget.TextView[@text='功能测试1']").click()
            #self.find_ele("id", "com.android.contacts:id/item").click()
            self.find_ele("id", "com.xihe.moblie.credit:id/conform").click()

            # 进行添加紧急联系人2信息
            self.find_ele("id", "com.xihe.moblie.credit:id/add2").click()
            self.sleep(1)
            self.find_ele("id", "com.xihe.moblie.credit:id/relationshap_item").click()
            self.find_ele("name", random.choice(relation)).click()
            self.find_ele("id", "com.xihe.moblie.credit:id/pickConnecter").click()
            #xpath2="//android.widget.RelativeLayout[contains(@id,'com.android.contacts:id/contacts_body')]//android.widget.ListView[contains(@id,'com.android.contacts:id/main_list')]//android.view.View[2]//android.widget.FrameLayout[contains(@id,'com.android.contacts:id/contact_list_item')]"
            self.find_ele("xpath", "//android.widget.TextView[@text='功能测试2']").click()
            #self.find_ele("id", "com.android.contacts:id/item").click()
            self.find_ele("id", "com.xihe.moblie.credit:id/conform").click()
            #单击确定添加紧急联系人
            self.find_ele("id", "com.xihe.moblie.credit:id/conform").click()
        else:
            #查看紧急联系人信息
            self.find_ele("id", "com.xihe.moblie.credit:id/user_info_connecter").click()
            self.find_ele("id", "com.xihe.moblie.credit:id/head_back").click()

        #单击返回到个人信息页面
        self.find_ele("id", "com.xihe.moblie.credit:id/head_back").click()

    def test_moreauth(self):
        self.wait_activity(".ui.activity.HomeActivity")
        log.debug("进入个人中心页面")
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_homeme").click()
        self.sleep(3)
        #单击个人信息
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_user_info").click()
        more=self.find_ele("id", "com.xihe.moblie.credit:id/tv_user_info_more").get_attribute("text")
        if more=='去完善':
            self.find_ele("id", "com.xihe.moblie.credit:id/user_info_more").click()
            #点击学历
            self.find_ele("id", "com.xihe.moblie.credit:id/more_educational").click()
            self.sleep(1)
            self.find_ele("name", random.choice(education)).click()
            self.sleep(1)
            # 点击婚姻
            self.find_ele("id", "com.xihe.moblie.credit:id/more_marriage").click()
            self.sleep(1)
            self.find_ele("name", random.choice(marriage)).click()
            self.sleep(1)
            # 点击地址
            self.find_ele("id", "com.xihe.moblie.credit:id/more_dizhi").click()
            #选择省市区
            self.find_ele("id", "com.xihe.moblie.credit:id/tv_select").click()
            self.sleep(1)
            self.find_ele("id","com.xihe.moblie.credit:id/btn_confirm").click()
            self.sleep(1)
            #输入详细地址
            self.find_ele("id", "com.xihe.moblie.credit:id/et_detailed_address").send_keys("address")
            self.sleep(1)
            #单击返回添加更多信息
            self.find_ele("id", "com.xihe.moblie.credit:id/head_back").click()
        else:
            #查看更多信息
            self.find_ele("id", "com.xihe.moblie.credit:id/user_info_more").click()
            self.find_ele("id", "com.xihe.moblie.credit:id/head_back").click()
        # 单击返回到个人信息页面
        self.find_ele("id", "com.xihe.moblie.credit:id/head_back").click()

    def test_bankcard(self):
        self.wait_activity(".ui.activity.HomeActivity")
        log.debug("进入个人中心页面")
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_homeme").click()
        self.sleep(1)
        self.find_ele("id","com.xihe.moblie.credit:id/ll_user_bank").click()
        if self.iselementexist("id","com.xihe.moblie.credit:id/btn_out_user"):
            self.find_ele("id","com.xihe.moblie.credit:id/btn_out_user").click()
            self.find_ele("id","com.xihe.moblie.credit:id/bankcard_et_input").send_keys("622578451234857485")
            self.find_ele("id","com.xihe.moblie.credit:id/tv_bankcard").click()
            self.find_ele("xpath","//android.view.View[@content-desc='  中国工商银行']").click()
            self.find_ele("id","com.xihe.moblie.credit:id/tv_bankcard_city").click()
            log.info(self.con())
            self.getH5()
            self.find_ele("id","gr_zone_ids").click()
            self.find_ele("xpath","//android.webkit.WebView/android.view.View[1]").click()
            self.find_ele("xpath", "//android.view.View[contains(@text,'北京')]").click()
            self.find_ele("id","subStaffLogin").click()
            self.find_ele("id","com.xihe.moblie.credit:id/bankcard_et_phone").send_keys(self.dic['username'])
            self.find_ele("id","com.xihe.moblie.credit:id/bankcard_bt_confirm").click()
        else:
            log.debug("银行卡信息已绑定")
            self.back()

    def test_borrow(self):
        self.wait_activity(".ui.activity.HomeActivity")
        log.debug("进入借款页")
        self.sleep(1)
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_borrowing").click()
        self.sleep(1)
        btn_text=self.find_ele("id","com.xihe.moblie.credit:id/btn_apply").get_attribute("text")
        if btn_text=='立即借款':
            width = self.size("width")
            imageview=self.find_eles("classname","android.widget.ImageView")
            print len(imageview)
            #申请金额滑动按钮
            moneybt=imageview[2]
            print moneybt
            moneylc=moneybt.location
            mxpoint = moneylc['x']
            print mxpoint
            mypoint = moneylc['y']
            print mypoint
            self.swip(mxpoint,mypoint,random.randint(mxpoint,width),mypoint)
            #借款期限滑动按钮
            daybt = imageview[3]
            print daybt
            daylc = daybt.location
            dxpoint = daylc['x']
            print dxpoint
            dypoint = daylc['y']
            print dypoint
            self.swip(dxpoint, dypoint, random.randint(dxpoint, width), dypoint)
            self.sleep(1)

            #单击立即借款按钮
            self.find_ele("id","com.xihe.moblie.credit:id/btn_apply").click()
            self.sleep(3)
            #判断是否有优惠券
            if self.iselementexist("id","com.xihe.moblie.credit:id/tv_content"):
                #有优惠券存在
                self.find_ele("id", "com.xihe.moblie.credit:id/tv_yes").click()
                self.withdiscount()

                if self.find_ele("id","com.xihe.moblie.credit:id/tv_on").click():
                    self.contract()
                elif self.find_ele("id","com.xihe.moblie.credit:id/tv_yes").click():
                    self.withdiscount()
            else:
                #查看合同并签署
                self.contract()
        else:
            log.info("有借款没有还款完成，不能进行借款")
            #查看借款记录
            #self.find_ele("id", "com.xihe.moblie.credit:id/btn_apply").click()

    #确认合同
    def contract(self):
        self.sleep(5)
        # 签署合同
        self.find_ele("classname", "android.widget.Button").click()
        self.sleep(1)
        # 查看借款记录信息
        #self.find_ele("id", "com.xihe.moblie.credit:id/tv_yes")

        self.back()

    #有优惠券，使用优惠券
    def withdiscount(self):
        self.sleep(3)
        #选择优惠券
        self.find_ele("id","com.xihe.moblie.credit:id/iv_bg").click()
        #进入试算页面
        self.sleep(1)
        self.find_ele("id","com.xihe.moblie.credit:id/btn_apply").click()
        self.contract()

    #正常还款
    def test_normalrefund(self):
        self.wait_activity(".ui.activity.HomeActivity")
        if self.iselementexist("id","com.xihe.moblie.credit:id/tv_yes"):
            self.find_ele("id","com.xihe.moblie.credit:id/tv_yes").click()
        log.debug("进入还款页面")
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_reimbursement").click()
        self.sleep(1)
        total_m=self.find_ele("id","com.xihe.moblie.credit:id/repay_total_count").get_attribute("text")
        # 修改数据库时间
        self.mysql.normalupdate(self.dic['username'])
        #全额还款

        self.find_ele("id","com.xihe.moblie.credit:id/pay_all").click()
        #确认还款
        self.find_ele("id","com.xihe.moblie.credit:id/conform").click()
        self.sleep(3)
        #输入还款验证码
        self.find_ele("id","com.xihe.moblie.credit:id/et_code").send_keys("0000")
        self.find_ele("id","com.xihe.moblie.credit:id/tv_yes").click()


    #提前还款
    def test_advancerefund(self):
        self.wait_activity(".ui.activity.HomeActivity")
        if self.iselementexist("id","com.xihe.moblie.credit:id/tv_yes"):
            self.find_ele("id","com.xihe.moblie.credit:id/tv_yes").click()
        log.debug("进入还款页面")
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_reimbursement").click()
        self.sleep(1)
        total_m = self.find_ele("id", "com.xihe.moblie.credit:id/repay_total_count").get_attribute("text")
        #修改数据库时间
        self.mysql.earlyupdate(self.dic['username'])
        # 提前还款
        self.find_ele("id", "com.xihe.moblie.credit:id/pay_all_advanced").click()
        # 确认还款
        self.find_ele("id", "com.xihe.moblie.credit:id/conform").click()
        self.sleep(3)
        # 输入还款验证码
        self.find_ele("id", "com.xihe.moblie.credit:id/et_code").send_keys("0000")
        self.find_ele("id", "com.xihe.moblie.credit:id/tv_yes").click()

    def test_loaninfo(self):
        #查看借款记录
        self.wait_activity(".ui.activity.HomeActivity")
        log.debug("进入个人中心页面")
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_homeme").click()
        self.sleep(2)
        self.find_ele("id","com.xihe.moblie.credit:id/iv_loan_history").click()
        self.sleep(1)
        self.find_ele("id","com.xihe.moblie.credit:id/head_back").click()

    def test_discount(self):
        self.wait_activity(".ui.activity.HomeActivity")
        log.debug("进入个人中心页面")
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_homeme").click()
        self.sleep(2)
        self.find_ele("id","com.xihe.moblie.credit:id/ll_coupon").click()
        self.sleep(1)
        self.find_ele("id","com.xihe.moblie.credit:id/head_back").click()

    def test_logout(self):
        #self.wait_activity(".activity.MainActivity")
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_homeme").click()
        self.sleep(1)
        self.find_ele("id", "com.xihe.moblie.credit:id/ll_seting").click()
        self.sleep(1)
        self.find_ele("id", "com.xihe.moblie.credit:id/btn_out_user").click()  # 安全退出

if __name__ == '__main__':
    ip="10.167.170.35"
    port="4723"
    apkname="Mobile_Phone_Credit-debug.apk"

    test=shoujidai(ip,port,apkname)
    test.stat_appium()
    test.test_login()
    test.test_borrow()
