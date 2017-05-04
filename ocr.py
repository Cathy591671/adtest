# coding=utf-8

#from base import base
from testbase import base
import logger as log
import command as cmd

class ocr(base):

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
        log.debug("进入欢迎页")
        self.sleep(4)
        width = self.size("width")
        log.info(width)
        height = self.size('height')
        log.info(height)
        self.swip(int(width) * 0.95, int(height) * 0.25, int(width) * 0.25, int(height) * 0.25)
        self.sleep(2)
        self.swip(int(width) * 0.95, int(height) * 0.25, int(width) * 0.25, int(height) * 0.25)
        self.sleep(2)
        lijitiyan=self.find_ele("id","com.xinhe.ocr:id/button")
        self.sleep(2)
        lijitiyan.click()
        self.sleep(2)
        juese=self.find_ele("id","com.xinhe.ocr:id/roll_huijin")
        self.sleep(1)
        juese.click()
        self.sleep(2)
        text=self.find_ele("id","com.xinhe.ocr:id/textView4").get_attribute("text")
        self.check_text("用户名",text)
        self.sleep(2)


    def xinjie_zixun(self):
        width = self.size("width")
        height = self.size('height')
        self.sleep(1)
        xinjie=self.find_ele("id","com.xinhe.ocr:id/btn1")
        xinjie.click()
        self.sleep(1)
        luruzixun=self.find_ele("id","com.xinhe.ocr:id/iv1")
        luruzixun.click()
        self.sleep(1)
        titile=self.find_ele("id","com.xinhe.ocr:id/tv_center").get_attribute("text")
        self.check_text("录入客户咨询",titile)
        self.sleep(1)
        idnum=self.find_ele("id","com.xinhe.ocr:id/bank_card_idcard_num")
        idnum.send_keys(self.dic['idnum'])
        customername=self.find_ele("id","com.xinhe.ocr:id/bank_card_name")
        customername.send_keys(self.dic['customername'].decode('utf-8'))
        gender=self.find_ele("id","com.xinhe.ocr:id/tv_sex")
        gender.click()
        male=self.find_ele("id","android:id/text1")
        male.click()
        huji=self.find_ele("id","com.xinhe.ocr:id/et_Register")
        huji.send_keys(self.dic['huji'].decode('utf-8'))

        tel=self.find_ele("id","com.xinhe.ocr:id/et_mobilephone")
        tel.send_keys(self.dic['tel'])
        self.sleep(1)
        self.swip(int(width) * 0.5, int(height) * 0.85, int(width) * 0.5, int(height) * 0.25)
        self.sleep(1)
        qianfajiguan=self.find_ele("id","com.xinhe.ocr:id/customer_office")
        qianfajiguan.send_keys(self.dic['qianfajiguan'].decode('utf-8'))

        youxiaoqixian1=self.find_ele("id","com.xinhe.ocr:id/customer_validity1")
        youxiaoqixian1.click()

        button1=self.find_ele("id","android:id/button1")
        button1.click()

        youxiaoqixian2=self.find_ele("id","com.xinhe.ocr:id/customer_validity2")
        youxiaoqixian2.click()

        changqi=self.find_ele("id","com.xinhe.ocr:id/tvAlert")
        changqi.click()

        next=self.find_ele("id","com.xinhe.ocr:id/but_next")
        next.click()
        self.sleep(1)
        titile=self.find_ele("id","com.xinhe.ocr:id/textView").get_attribute("text")
        self.check_text("客户投资信息",titile)

        kehulaiyuan=self.find_ele("id","com.xinhe.ocr:id/tv_source")
        kehulaiyuan.click()

        xiaoshoukaifa=self.find_ele("id","android:id/text1")
        xiaoshoukaifa.click()

        jiekuanjine=self.find_ele("id","com.xinhe.ocr:id/et_planLoanMoney")
        jiekuanjine.send_keys(self.dic['jiekuanjine'])
        jiekuanqixian=self.find_ele("id","com.xinhe.ocr:id/et_planLoanTime")
        jiekuanqixian.send_keys(self.dic['jiekuanqixian'])
        hangye=self.find_ele("id","com.xinhe.ocr:id/tv_industry")
        hangye.click()

        self.find_ele("id","android:id/text1").click()
        self.sleep(1)
        yongtu=self.find_ele("id","com.xinhe.ocr:id/tv_loanUse")
        yongtu.click()

        self.find_ele("id","android:id/text1").click()
        self.find_ele("id","com.xinhe.ocr:id/et_communication").send_keys(self.dic['goutong'].decode('utf-8'))
        self.find_ele("id","com.xinhe.ocr:id/but_next").click()
        self.sleep(1)
        titile=self.find_ele("id","com.xinhe.ocr:id/textView8").get_attribute("text")
        self.check_text("银行卡信息",titile)
        self.sleep(1)
        self.find_ele("id","com.xinhe.ocr:id/but_finish").click()
        self.sleep(1)

    def xinjie_bulu(self):
        width = self.size("width")
        height = self.size('height')
        self.find_ele("id","com.xinhe.ocr:id/btn1").click()
        self.sleep(1)
        self.find_ele("id","com.xinhe.ocr:id/iv2").click()
        self.sleep(1)
        self.find_ele("id","com.xinhe.ocr:id/iv3").click()
        self.sleep(1)

        customername=self.find_ele("id","com.xinhe.ocr:id/name")
        customername.send_keys(self.dic['customername'].decode('utf-8'))
        idnum=self.find_ele("id","com.xinhe.ocr:id/certNum")
        idnum.send_keys(self.dic['idnum'])
        self.find_ele("id","com.xinhe.ocr:id/bank_card_serch").click()
        self.sleep(10)
        self.find_ele("id","com.xinhe.ocr:id/iv_registeredResidenceNature").click()
        self.sleep(1)
        self.find_ele("id","android:id/text1").click()
        self.sleep(1)
        self.swip(int(width) * 0.5, int(height) * 0.85, int(width) * 0.5, int(height) * 0.25)
        self.sleep(1)
        self.find_ele("id","com.xinhe.ocr:id/iv_maritalStatus").click()
        self.sleep(1)
        self.find_ele("id","android:id/text1").click()
        self.sleep(1)
        self.find_ele("id","com.xinhe.ocr:id/iv_apply_schoolrecord").click()
        self.find_ele("id","android:id/text1").click()
        self.find_ele("id","com.xinhe.ocr:id/iv_Addr").click()
        self.find_ele("id","android:id/button1").click()
        xiangxidizhi=self.find_ele("id","com.xinhe.ocr:id/et_presentDetailAddress")
        xiangxidizhi.send_keys(self.dic['xiangxi'].decode('utf-8'))
        self.find_ele("id","com.xinhe.ocr:id/but_next").click()
        self.sleep(1)
        zinv=self.find_ele("id","com.xinhe.ocr:id/et_childNum")
        zinv.send_keys(self.dic['zinv'])
        gongyang=self.find_ele("id","com.xinhe.ocr:id/et_provideNum")
        gongyang.send_keys(self.dic['gongyang'])
        nianshouru=self.find_ele("id","com.xinhe.ocr:id/et_personYearIncome")
        nianshouru.send_keys(self.dic['nianshouru'])
        yueshouru=self.find_ele("id","com.xinhe.ocr:id/et_familyMonthIncome")
        yueshouru.send_keys(self.dic['yueshouru'])
        yuezhichu=self.find_ele("id","com.xinhe.ocr:id/et_familyMonthPay")
        yuezhichu.send_keys(self.dic['yuezhichu'])
        fuzhai=self.find_ele("id","com.xinhe.ocr:id/et_familyTotalLiability")
        fuzhai.send_keys(self.dic['fuzhai'])

        zhaidian=self.find_ele("id","com.xinhe.ocr:id/et_houseTel")
        zhaidian.send_keys(self.dic['zhaidian'])
        self.sleep(1)
        self.swip(int(width) * 0.5, int(height) * 0.85, int(width) * 0.5, int(height) * 0.25)
        self.sleep(1)
        mail=self.find_ele("id","com.xinhe.ocr:id/et_email")
        mail.send_keys(self.dic['mail'])

        self.find_ele("id","com.xinhe.ocr:id/iv_residenceType").click()
        self.find_ele("id","android:id/text1").click()

        self.find_ele("id","com.xinhe.ocr:id/iv_beginComeCityTime").click()
        self.find_ele("id","android:id/button1").click()

        self.find_ele("id","com.xinhe.ocr:id/iv_beginLiveTime").click()
        self.find_ele("id","android:id/button1").click()

        self.find_ele("id","com.xinhe.ocr:id/iv_CustomerSource").click()

        #xpath双选
        laiyuan0=self.find_ele("xpath","//android.widget.CheckedTextView[contains(@index,0)]")
        laiyuan1=self.find_ele("xpath","//android.widget.CheckedTextView[contains(@index,1)]")
        laiyuan0.click()
        laiyuan1.click()

        self.find_ele("id","android:id/button2").click()

        self.find_ele("id","com.xinhe.ocr:id/iv_customerDiff").click()
        self.find_ele("id","android:id/text1").click()

        self.find_ele("id","com.xinhe.ocr:id/but_next").click()
        self.sleep(1)

        self.find_ele("id","com.xinhe.ocr:id/iv_productType").click()
        self.find_ele("id","android:id/text1").click()

        shenqingedu=self.find_ele("id","com.xinhe.ocr:id/et_applyAmount")
        shenqingedu.send_keys(self.dic['shenqingedu'])

        self.find_ele("id","com.xinhe.ocr:id/iv_planLoanTime").click()
        self.find_ele("id","android:id/text1").click()

        zuigaochengshou=self.find_ele("id","com.xinhe.ocr:id/et_mostHighMoneyPay")
        zuigaochengshou.send_keys(self.dic['zuigaochengshou'])

        self.find_ele("id","com.xinhe.ocr:id/iv_payMoneySource").click()
        self.find_ele("id","android:id/text1").click()

        self.find_ele("id","com.xinhe.ocr:id/iv_loanUse").click()
        self.find_ele("id","android:id/text1").click()

        self.find_ele("id","com.xinhe.ocr:id/iv_qitalaiyuan").click()
        self.find_ele("id","android:id/text1").click()
        self.find_ele("id","android:id/button2").click()
        self.sleep(1)
        self.swip(int(width) * 0.5, int(height) * 0.85, int(width) * 0.5, int(height) * 0.25)
        self.sleep(1)
        qita=self.find_ele("id","com.xinhe.ocr:id/et_otherMonthIncome")
        qita.send_keys(self.dic['qita'])

        bishu=self.find_ele("id","com.xinhe.ocr:id/et_rePayBorrowMoneyTotalNum")
        bishu.send_keys(self.dic['bishu'])

        self.find_ele("id","com.xinhe.ocr:id/iv_urgent").click()
        self.find_ele("id","android:id/text1").click()

        yuehuankuan=self.find_ele("id","com.xinhe.ocr:id/et_monthPayTotalAccount")
        yuehuankuan.send_keys(self.dic['yuehuankuan'])

        self.find_ele("id","com.xinhe.ocr:id/but_next").click()
        self.sleep(1)

        qinshuname=self.find_ele("id","com.xinhe.ocr:id/et_relativesName")
        qinshuname.send_keys(self.dic['qinshuname'].decode('utf-8'))

        self.find_ele("id","com.xinhe.ocr:id/iv_relationA").click()
        self.find_ele("id","android:id/text1").click()

        qinshuntel=self.find_ele("id","com.xinhe.ocr:id/et_relativesTel")
        qinshuntel.send_keys(self.dic['qinshuntel'])

        workzhengmingren=self.find_ele("id","com.xinhe.ocr:id/et_workProvePerson")
        workzhengmingren.send_keys(self.dic['workzhengmingren'].decode('utf-8'))

        self.find_ele("id","com.xinhe.ocr:id/iv_relationB").click()
        self.find_ele("id","android:id/text1").click()

        zhiwu=self.find_ele("id","com.xinhe.ocr:id/et_workProvePersonPost")
        zhiwu.send_keys(self.dic['zhiwu'].decode('utf-8'))

        bumen=self.find_ele("id","com.xinhe.ocr:id/et_workProvePersonDepartment")
        bumen.send_keys(self.dic['bumen'].decode('utf-8'))

        workzhengmingtel=self.find_ele("id","com.xinhe.ocr:id/et_workProvePersonTel")
        workzhengmingtel.send_keys(self.dic['workzhengmingtel'])
        self.sleep(1)
        self.swip(int(width) * 0.5, int(height) * 0.85, int(width) * 0.5, int(height) * 0.25)
        self.sleep(1)
        qita1name=self.find_ele("id","com.xinhe.ocr:id/et_otherContactMan1")
        qita1name.send_keys(self.dic['qita1name'].decode('utf-8'))

        guanxi1=self.find_ele("id","com.xinhe.ocr:id/et_otherContactManRelation1")
        guanxi1.send_keys(self.dic['guanxi1'].decode('utf-8'))

        qita1tel=self.find_ele("id","com.xinhe.ocr:id/et_otherContactManTel1")
        qita1tel.send_keys(self.dic['qita1tel'])

        qita2name=self.find_ele("id","com.xinhe.ocr:id/et_otherContactMan2")
        qita2name.send_keys(self.dic['qita2name'].decode('utf-8'))

        guanxi2=self.find_ele("id","com.xinhe.ocr:id/et_otherContactManRelation2")
        guanxi2.send_keys(self.dic['guanxi2'].decode('utf-8'))

        qita2tel=self.find_ele("id","com.xinhe.ocr:id/et_otherContactManTel2")
        qita2tel.send_keys(self.dic['qita2tel'])

        self.find_ele("id","com.xinhe.ocr:id/but_next").click()
        self.sleep(1)

        self.find_ele("id","com.xinhe.ocr:id/iv_householderRelation").click()
        self.find_ele("id","android:id/text1").click()

        self.find_ele("id","com.xinhe.ocr:id/iv_Addr").click()
        self.find_ele("id","android:id/button1").click()

        xiangxidz=self.find_ele("id","com.xinhe.ocr:id/et_householderDetailAddress")
        xiangxidz.send_keys(self.dic['xiangxidz'].decode('utf-8'))

        self.find_ele("id","com.xinhe.ocr:id/but_next").click()
        self.sleep(1)

        danweiname=self.find_ele("id","com.xinhe.ocr:id/et_company")
        danweiname.send_keys(self.dic['danweiname'].decode('utf-8'))

        self.find_ele("id","com.xinhe.ocr:id/iv_companyAddr").click()
        self.find_ele("id","android:id/button1").click()

        danweidizhi=self.find_ele("id","com.xinhe.ocr:id/et_companyDetailAddress")
        danweidizhi.send_keys(self.dic['danweidizhi'].decode('utf-8'))

        danweidianhua=self.find_ele("id","com.xinhe.ocr:id/et_companyPhone")
        danweidianhua.send_keys(self.dic['danweidianhua'])

        fenjihao=self.find_ele("id","com.xinhe.ocr:id/et_companyPhoneExt")
        fenjihao.send_keys(self.dic['fenjihao'])

        self.find_ele("id","com.xinhe.ocr:id/iv_companyType").click()
        self.find_ele("id","android:id/text1").click()

        self.find_ele("id","com.xinhe.ocr:id/iv_industry").click()
        self.find_ele("id","android:id/text1").click()
        self.sleep(1)
        self.swip(int(width) * 0.5, int(height) * 0.85, int(width) * 0.5, int(height) * 0.25)
        self.sleep(1)
        self.find_ele("id","com.xinhe.ocr:id/iv_postLevel").click()
        self.find_ele("id","android:id/text1").click()

        zhiyezhiwu=self.find_ele("id","com.xinhe.ocr:id/et_post")
        zhiyezhiwu.send_keys(self.dic['zhiyezhiwu'].decode('utf-8'))

        self.find_ele("id","com.xinhe.ocr:id/tv_entryCompanyTime").click()
        self.find_ele("id","android:id/button1").click()

        zhiyebumen=self.find_ele("id","com.xinhe.ocr:id/et_department")
        zhiyebumen.send_keys(self.dic['zhiyebumen'].decode('utf-8'))

        self.find_ele("id","com.xinhe.ocr:id/iv_faxin").click()
        self.find_ele("id","android:id/text1").click()

        self.find_ele("id","com.xinhe.ocr:id/iv_payday").click()
        self.find_ele("id","android:id/text1").click()

        qiandanwei=self.find_ele("id","com.xinhe.ocr:id/et_beforeCompanyName")
        qiandanwei.send_keys(self.dic['qiandanwei'].decode('utf-8'))

        yuangongshuliang=self.find_ele("id","com.xinhe.ocr:id/et_staffAmount")
        yuangongshuliang.send_keys(self.dic['yuangongshuliang'])


        shuihougongzi=self.find_ele("id","com.xinhe.ocr:id/et_compSalary")
        shuihougongzi.send_keys(self.dic['shuihougongzi'])

        self.find_ele("id","com.xinhe.ocr:id/but_next").click()
        self.sleep(1)

        yinhangka=self.find_ele("id","com.xinhe.ocr:id/et_accountId")
        yinhangka.send_keys(self.dic['yinhangka'])

        self.find_ele("id","com.xinhe.ocr:id/iv_accountBank").click()
        self.find_ele("id","android:id/text1").click()

        zhihang=self.find_ele("id","com.xinhe.ocr:id/customer_card_bankbrach")
        zhihang.send_keys(self.dic['zhihang'].decode('utf-8'))

        self.find_ele("id","com.xinhe.ocr:id/iv_accountRegion").click()
        self.find_ele("id","android:id/button1").click()

        self.find_ele("id","com.xinhe.ocr:id/iv_signingPlatform").click()
        self.find_ele("id","android:id/text1").click()
        self.find_ele("id","com.xinhe.ocr:id/but_commit").click()
        self.sleep(2)





























    def test_login(self):
        name=self.find_ele("id","com.xinhe.ocr:id/user_name")
        name.send_keys(self.dic['name'])
        password=self.find_ele("id","com.xinhe.ocr:id/pwd")
        password.send_keys(self.dic['password'])
        login=self.find_ele("id","com.xinhe.ocr:id/but_longin")
        login.click()
        self.sleep(1)
        yes=self.find_ele("id","com.xinhe.ocr:id/Yes")
        yes.click()
        self.sleep(1)

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


