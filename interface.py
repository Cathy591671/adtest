#coding:utf-8
import requests
import logger as log
import mysqlexe
from requests_toolbelt import MultipartEncoder

ip = '10.167.200.64:8081'

mysql=mysqlexe.mysql()

def login(username,password):
    res=[]
    loginpara = {'userName': username, 'passWord': password}
    l = requests.post('http://' + ip + '/MBSPcreditharmony-SJDWeb/mobileUser/login.do', params=loginpara)
    content = l.json()
    print content
    msg=content['message'].encode('utf-8')
    log.info(msg)
    res.append(msg)
    if msg=='登录成功':
        cus = content['customer']
        userid = cus['id']
        res.append(userid)
        token = content['token']
        res.append(token)
    print res
def getcode():
    codepara = {'phoneNum': username, 'isRegister': '1'}
    r = requests.post('http://' + ip + '/MBSPcreditharmony-SJDWeb/mobileUser/sendValidCode.do', params=codepara)
    content = r.json()
    log.info(content['message'])
    code = mysql.valicode()
    return code

def regist(username,password):
    code=getcode()
    registpara={'userName':username,'passWord':password,'validCode':code}
    re=requests.post('http://'+ip+'/MBSPcreditharmony-SJDWeb/mobileUser/register.do',params=registpara)
    content = re.json()
    log.info( content['message'])
    log1=login(username,password)
    userid=log1[1]
    log.info(userid)
    token= log1[2]
    log.info(token)
    #headers = {'Content-Type': 'multipart/form-data','token':token}
    personPic={'file': open('C:\Users\Public\Pictures\idcard\lijia.jpg', 'rb')}
    cardFrontPic={'file': open('C:\Users\Public\Pictures\idcard\lijia.jpg', 'rb')}
    cadHeadPic={'file': open('C:\Users\Public\Pictures\idcard\lijia.jpg', 'rb')}
    cardBackPic={'file': open('C:\Users\Public\Pictures\idcard\\back.jpg', 'rb')}
    m = MultipartEncoder(fields={'userId':userid,'name':'李佳','identityNum':'421083198509081218','nation':'汉','address':'湖北省3-27',
              'sex':'男','cardTime':'20070416-20270416','valideOrg':'新沂市公安局','birthday':'1985-09-08','token':token,
                             'personPic': ('filename',open('C:\Users\Public\Pictures\idcard\lijia.jpg', 'rb'), 'image/jpg'),
                            'cardFrontPic': ('filename', open('C:\Users\Public\Pictures\idcard\lijia.jpg', 'rb'),'image/jpg'),
                            'cadHeadPic': ('filename', open('C:\Users\Public\Pictures\idcard\lijia.jpg', 'rb'),'image/jpg'),
                            'cardBackPic': ('filename', open('C:\Users\Public\Pictures\idcard\\back.jpg', 'rb'),'image/jpg')
                        }
                    )
    headers = {'Content-Type': m.content_type,'token':token}
    infopara={'userId':userid,'name':'李佳','identityNum':'421083198509081218','nation':'汉','address':'湖北省1023',
              'sex':'男','birthday':'1985-09-08','cardTime':'20070227-20270227','valideOrg':'东阳市公安局',
              'personPic':personPic,'cardFrontPic':cardFrontPic,'cardBackPic':cardBackPic,'cadHeadPic':cadHeadPic}
    info=requests.post('http://'+ip+'/MBSPcreditharmony-SJDWeb/customer/saveCustomerInfo.do',data=m,headers=headers)
    #info = requests.post('http://' + ip + '/MBSPcreditharmony-SJDWeb/customer/saveCustomerInfo.do', params=infopara,headers=headers)

    #print info.status_code
    #print info.text
    #print l.json()
    content = info.json()
    log.info( content['message'])

def check(username,password):
    ll=login(username,password)
    log.info(ll)
    msg=ll[0]
    if msg == '用户名不存在':
        log.debug('用户还没有注册，进行注册')
        regist(username,password)

def verify(username, password):
    log1 = login(username, password)
    userid = log1[1]
    log.info(userid)
    token = log1[2]
    log.info(token)
    # headers = {'Content-Type': 'multipart/form-data','token':token}
    '''
    personPic = {'file': open('C:\Users\Public\Pictures\idcard\lijia.jpg', 'rb')}
    cardFrontPic = {'file': open('C:\Users\Public\Pictures\idcard\lijia.jpg', 'rb')}
    cadHeadPic = {'file': open('C:\Users\Public\Pictures\idcard\lijia.jpg', 'rb')}
    cardBackPic = {'file': open('C:\Users\Public\Pictures\idcard\\back.jpg', 'rb')}
    infopara = {'userId': userid, 'name': '李佳', 'identityNum': '421083198509081218', 'nation': '汉',
                'address': '湖北省1023',
                'sex': '男', 'birthday': '1985-09-08', 'cardTime': '20070227-20270227', 'valideOrg': '东阳市公安局',
                'personPic': personPic, 'cardFrontPic': cardFrontPic, 'cardBackPic': cardBackPic,
                'cadHeadPic': cadHeadPic}
    '''
    m = MultipartEncoder(fields={'userId': userid, 'name': '李佳', 'identityNum': '421083198509081218', 'nation': '汉',
                                 'address': '湖北省3-27',
                                 'sex': '男', 'cardTime': '20070416-20270416', 'valideOrg': '新沂市公安局',
                                 'birthday': '1985-09-08', 'token': token,
                                 'personPic': (
                                 'filename', open('C:\Users\Public\Pictures\idcard\lijia.jpg', 'rb'), 'image/jpg'),
                                 'cardFrontPic': (
                                 'filename', open('C:\Users\Public\Pictures\idcard\lijia.jpg', 'rb'), 'image/jpg'),
                                 'cadHeadPic': (
                                 'filename', open('C:\Users\Public\Pictures\idcard\lijia.jpg', 'rb'), 'image/jpg'),
                                 'cardBackPic': (
                                 'filename', open('C:\Users\Public\Pictures\idcard\\back.jpg', 'rb'), 'image/jpg')
                                 }
                         )
    headers = {'Content-Type': m.content_type, 'token': token}
    info = requests.post('http://' + ip + '/MBSPcreditharmony-SJDWeb/customer/saveCustomerInfo.do', data=m,
                         headers=headers)
    # info = requests.post('http://' + ip + '/MBSPcreditharmony-SJDWeb/customer/saveCustomerInfo.do', params=infopara,headers=headers)

    # print info.status_code
    # print info.text
    # print l.json()
    content = info.json()
    log.info(content['message'])


if __name__ == '__main__':
    username="13800000000"
    psw="123456"
    login(username,psw)



