#  coding=utf-8
import os
import subprocess
import time
import logger as log
import shutil
import re
import sys
defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

log_path=os.getcwd()+"\\log"
file_path=os.getcwd()+"\\file"
img_path=os.getcwd()+"\\img"
def checkpath():
    if os.path.exists(file_path):
        pass
    else:
        os.mkdir(file_path)
    if os.path.exists(img_path):
        pass
    else:
        os.mkdir(img_path)
        
def adbkill():
    log.debug("开始关闭adb服务")
    kill_cmd = "adb kill-server"
    log.info("关闭adb服务的指令是：" + kill_cmd)
    os.popen(kill_cmd)

def adbstart():
    log.debug("开始启动adb服务")
    start_cmd = "adb start-server"
    log.info("关闭adb服务的指令是：" + start_cmd)
    os.popen(start_cmd)

def adbcon(ip):
    #os.system("adb kill-server")
    log.debug("开始连接手机，ip为:"+ip)
    con_cmd="adb connect %s"%(ip)
    log.info("手机连接的指令是：" + con_cmd)
    con_info=os.popen(con_cmd).read()
    #con_info=os.system(con_cmd)
    #print con_info.read()
    if "unable" in con_info:
        log.error("请查看手机ip正确，并且安装了wireless")
        return False
    else:
        iscon=adbdev(ip)
        if "unauthorized" in iscon or "offline" in iscon:
            log.debug("重新连接")
            adbcon(ip)
            #return False
        else:
            log.info("ip为:"+ip+"的手机连接成功")
        return True
'''
def adbcon(ip):
    #os.system("adb kill-server")
    log.debug("开始连接手机，ip为:"+ip)
    con_cmd="adb connect %s"%(ip)
    log.info("手机连接的指令是：" + con_cmd)
    con_info = os.popen(con_cmd).read()
    #print con_info.read()
    iscon=adbdev(ip)
    if "unauthorized" in iscon or "offline" in iscon:
        log.debug("重新连接")
        adbcon(ip)
    else:
        log.debug("ip为:"+ip+"的手机连接成功")
'''

def adbdev(ip):
    check_cmd="adb devices|findstr %s" %(ip)
    log.info("检查连接状态的指令为："+  check_cmd)
    check_info=os.popen(check_cmd).read()
    print check_info
    log.info("连接信息为:"+check_info)
    return check_info

def adbmdev():
    check_cmd="adb devices"
    log.info("检查所有连接的设备指令为："+  check_cmd)
    check_info=os.popen(check_cmd)
    log.info(check_info)
    #log.info("连接信息为:"+check_info)
    return check_info

def checkip(ip):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip):
        return True
    else:
        return False

def phonecon(way,ip):
    if way == "1":
        #log.debug("链接方式为"+way)
        return ip+':5555'
    elif way=="2":
        #log.debug("链接方式为" + way)
        return ip
    else:
        if checkip(ip):
            return ip+':5555'
        else:
            return ip

def adbgetversion(way,ip):
    getversion_cmd="adb -s "+ phonecon(way,ip)+"  shell getprop ro.build.version.release"
    log.info("获取安卓版本号的指令为："+  getversion_cmd)
    getversion_info=os.popen(getversion_cmd).read()
    log.info("安卓版本号:"+getversion_info)
    return getversion_info.strip()

def adbgetpro(way,ip):
    getprono_cmd="adb  -s "+ phonecon(way,ip)+"  shell getprop ro.product.model"
    log.info("获取安卓手机型号的指令为："+  getprono_cmd)
    getprono_info=os.popen(getprono_cmd).read()
    log.info("安卓手机型号:"+getprono_info)
    return getprono_info.strip()

def adblogcat(way,ip,packageName):
    tm = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    log.debug("开始获取log日志")
    log_filename =log_path+"\\"+ip+"#"+tm+"logcat.log"
    logcat_file = open(log_filename, 'w')
    #search the pid of packagename
    ps_cmd = "adb -s " + phonecon(way, ip) + "  shell ps|findstr %s" % (packageName)
    log.info(ps_cmd)
    ps_info = os.popen(ps_cmd)
    str = ""
    for i in ps_info.readlines():
        log.info(i)
        pid_list = i.split()
        log.info(pid_list)
        pid = pid_list[1]
        log.info(pid)
        str = ' '.join([str, pid.strip()])
        #str = str + " " + pid
    '''
    pid_cmd = "adb -s "+ phonecon(way,ip)+"  shell busybox pgrep %s"%(packageName)
    log.info("查找包名为"+packageName+"的pid指令为："+ pid_cmd)
    pid_info=os.popen(pid_cmd)
    #print pid_info
    #print len(pid_info.read())
    str=""
    for pid in pid_info:
        log.info("IP为 %s 包为 %s 的pid为： " % (ip, packageName) + pid.strip())
        str = ' '.join([str, pid.strip()])
    '''
    if str.strip()=="":
        log.info("包名为 %s 的进程没有启动，获取不到pid" % (packageName))
        log_cmd = "adb -s "+ phonecon(way,ip)+"  logcat -v time"
        log.info("打印所有进程的日志的指令为：" + log_cmd)
        log_info = subprocess.Popen(log_cmd, stdout=logcat_file, stderr=subprocess.PIPE)
        #print log_info
        time.sleep(10)
        log_info.terminate()
        log.debug("设备ip为"+ip+"的日志打印完成")
    else:
        log_cmd = "adb -s "+ phonecon(way,ip)+"  logcat -v time *:E |findstr '%s' " % (str)
        log.info("打印设备ip为%s的日志指令为：" % (ip) + log_cmd)
        log_info = subprocess.Popen(log_cmd, stdout=logcat_file, stderr=subprocess.PIPE)
        #print log_info
        #time.sleep(10)
        log_info.wait()
        log_info.terminate()
        log.debug("设备ip为" + ip + "的日志打印完成")

def adbuninstall(way,ip,packageName):
    log.debug("检查设备ip为"+ip+"的手机上是否安装了包"+packageName)
    find_cmd="adb -s "+ phonecon(way,ip)+"  shell pm list package|findstr %s"%(packageName)
    log.info("检查是否安装包的指令为：" + find_cmd)
    find_info=os.popen(find_cmd)
    length= len(find_info.read())
    #print len(find_info.read()), length <= 0
    if length <= 0 :
        log.info("设备ip为%s上没有安装包%s"%(ip,packageName))
    else:
        log.info("设备ip为%s上安装了包%s"%(ip,packageName))
        log.debug("开始卸载包")
        uninstall_cmd="adb -s "+ phonecon(way,ip)+"  shell pm uninstall %s"%(packageName)
        log.info("卸载包的命令为：" + uninstall_cmd)
        uninstall_info=os.popen(uninstall_cmd)
        print uninstall_info.read()
        log.debug("卸载包完成")

def svncheck(svnpath):
    update_cmd = 'svn update '+svnpath
    updateinfo=os.popen(update_cmd)
    time.sleep(5)
    x=str(updateinfo.read())
    log.info( '打印的日志是'+x)
    if 'A    '+svnpath in x:
        xsp=x.split('A    '+svnpath+'\\')[1].split('.apk')[0]
        log.info( 'xsp是'+xsp)
        global apkname
        apkname=str(xsp)+'.apk'
        log.info( '更新的包是:'+apkname)
        log.info("更改config文件中的包名")
        f = open(file_path+'\config.txt', 'r+')
        flist = f.readlines()
        flist[3] = 'apkname'+'|'+apkname
        f = open(file_path+'\config.txt', 'w+')
        f.writelines(flist)
        log.info("复制文件到file文件夹中")
        shutil.move(svnpath+'\\'+apkname,file_path+'\\'+apkname)
        f.close()
        return apkname


def adbinstall(way,ip,name):
    log.debug("在设备ip为"+ip+"上开始安装"+name)
    #install_cmd='adb -s "+ phonecon(way,ip)+"  shell pm install D:\python\\apk\%s'%(ip,name)
    install_cmd = "adb -s "+ phonecon(way,ip)+"  install -l -r %s\%s" % (file_path,name)
    log.info("安装指令为" + install_cmd)
    install_info= subprocess.Popen(install_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    log.info("安装进行中")
    out=install_info.stdout.read()
    err=install_info.stderr.read()
    log.info(out)
    if err !="":
        log.error(err)

def startappium(ip,port):
    log.debug("为IP为"+ip+"开始启动appium服务")
    bpport = int(port) + 1
    #print "the bpport is "+ str(bpport)
    #startappium_cmd="start /b appium -a 127.0.0.1 -p %s --bootstrap-port %s --log %s\%s.log"%(port,str(bpport),log_path,port)
    startappium_cmd = "start /b appium -a 127.0.0.1 -p %s -bp %s --log %s\%s.log" % (port, str(bpport), log_path, port)
    log.info("启动appium的指令为：" + startappium_cmd)
    srartappium_info=os.system(startappium_cmd)
    #srartappium_info = subprocess.Popen(startappium_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    #srartappium_info.wait()
    list_cmd = "tasklist |findstr node"
    #print list_cmd
    list_info = os.popen(list_cmd)
    log.info(list_info.read())
    log.debug("IP为"+ip+"启动appium服务完成")
    time.sleep(60)

def adbinput(way,ip,text):
    input_cmd = "adb  -s "+ phonecon(way,ip)+"  shell input text %s" % (text)
    log.info("输入的指令为：" + input_cmd)
    input_info = os.popen(input_cmd)
    print input_info.read()

def killappium():
    cmd = "taskkill /F /im node.exe"
    log.debug("杀进程Node.exe")
    task_info = os.popen(cmd)

def killadb():
    cmd = "taskkill /F /im adb.exe"
    log.debug("杀进程adb.exe")
    task_info = os.popen(cmd)

def killpid(port):
    pid='555'
    cmd = "taskkill /F /PID %s"%(pid)
    log.debug("杀pid为"+pid+"的进程")
    task_info = os.popen(cmd)

def adbmeninfo(way,ip,packageName):
    tm = time.strftime('%d-%H-%M-%S', time.localtime(time.time()))
    men_cmd = "adb  -s "+ phonecon(way,ip)+"  shell dumpsys meminfo %s>%s/%s%s-men.txt" % (packageName,log_path,ip,tm)
    log.info("输入的指令为：" + men_cmd)
    input_info = os.popen(men_cmd)
    #print input_info.read()

def adbcpuinfo(way,ip,packageName):
    tm = time.strftime('%d-%H-%M-%S', time.localtime(time.time()))
    cpu_cmd = "adb  -s "+ phonecon(way,ip)+"  shell dumpsys cpuinfo|findstr %s >%s/%s%s-cpu.txt" % (packageName,log_path,ip,tm)
    log.info("输入的指令为：" + cpu_cmd)
    input_info = os.popen(cpu_cmd)

def adbtopinfo(way,ip):
    cpu_cmd = "adb  -s "+ phonecon(way,ip)+"  shell top -m 500 -d 2>%s/%s-top.txt" % (log_path,ip)
    log.info("输入的指令为：" + cpu_cmd)
    input_info = os.popen(cpu_cmd)

#--pct-syskeys 系统时间，back建，home建，音量键，电话键
#--pct-motion  滑动
def adbmonkey(way,ip,packageName,times):
    monkey_cmd="adb -s "+ phonecon(way,ip)+"  shell monkey -p %s --ignore-crashes --ignore-timeouts --pct-touch 30 --pct-syskeys 0 --pct-motion 0 -v -v --throttle 200 %s >%s/%s-monkey.txt"%(packageName,times,log_path,ip)
    log.info("执行monkey的指令为:"+monkey_cmd)
    os.popen(monkey_cmd)

#手机必须root才能使用
def adbnet(way,ip,packageName):
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    #获取app应用的uid
    uid_cmd="adb -s "+ phonecon(way,ip)+"  shell su -c cat /data/system/packages.list|grep %s"%(packageName)
    log.info(uid_cmd)
    uid_info = subprocess.Popen(uid_cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    uid=""
    for i in uid_info.stdout.readlines():
        log.info(i)
        uid_list=i.split()
        log.info(uid_list)
        uid=uid_list[1]
        log.info(uid)
    #uid=uid_info.stdout.readline()[1]
    log.info(uid)
    #获取app应用消耗的流量
    netfile = log_path + "\\" + uid + '-net.txt'
    net_cmd = "adb -s "+ phonecon(way,ip)+"  shell cat /proc/net/xt_qtaguid/stats |grep %s"%(uid)
    log.info(net_cmd)
    p = subprocess.Popen(net_cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    rx_b = 0
    tx_b = 0
    #log.info(p.stdout.readlines())
    for i in p.stdout.readlines():
        log.info(i)
        info = i.split()
        log.info(info)
        rx_b += int(info[5])
        log.info(rx_b)
        tx_b += int(info[7])
        log.info(tx_b)
    rxtx= rx_b + tx_b
    log.info(rxtx)
    fo=open(netfile, 'a')
    #运行一次，将数据保存到文件中
    fo.write(currentTime + ',' + str(rx_b) + ','+ str(tx_b)+ ','+str(rxtx) +'\n')

def adbelectric(way,ip,packagename):
    ps_cmd="adb -s "+ phonecon(way,ip)+"  shell ps|findstr %s"%(packagename)
    log.info(ps_cmd)
    ps_info = os.popen(ps_cmd)
    uid=""
    for i in ps_info.readlines():
        log.info(i)
        uid_list = i.split()
        log.info(uid_list)
        uid = uid_list[0].replace("_","")
        log.info(uid)
    elec_cmd="adb -s "+ phonecon(way,ip)+"  shell dumpsys batterystats %s |findstr %s"%(packagename,uid)
    log.info(elec_cmd)
    elec_info=os.popen(elec_cmd)
    log.info(elec_info.readline())

def texttodic(filename):
    log.debug("将文本转化为字典类型")
    datafile = file_path+filename
    log.info(datafile)
    if os.path.exists(datafile):
        f = open(datafile)
        dic = dict()
        key = ""
        lines = f.readlines()
        log.info(lines)
        for l in lines:
            if l.startswith('#'):
                key = l.strip('\n').strip('#').lower()
            else:

                line = l.strip().split('|')
                print line
                if key in dic:

                    dic[key].update({line[0].lower(): line[1]})
                else:

                    dic.update({key: {line[0].lower(): line[1]}})
        f.close()
        return dic
    else:
        log.error(datafile + "文件不存在")

def texttolist(filename):
    log.debug('将文本转化为列表类型')
    datafile=file_path+filename
    log.info(datafile)
    if os.path.exists(datafile):
        f=open(datafile)
        list=[]
        lines = f.readlines()
        for l in lines:
            list.append(l.strip())
        f.close()
        return list
    else:
        log.error(datafile + "文件不存在")

def analyzelog():
    log.debug("分析monkey的log日志")
    monlog=log_path+"//10.167.170.302017-03-03-17-35logcat.log"
    beffile=open(monlog,'r')
    content=beffile.readlines()
    beffile.close()

    with open(log_path+"//monkey.txt", 'a') as aftfile:
        # 分析日志文件中的问题
        str1 = '.*ANR.*'
        str2 = '.*CRASH.*'
        str3 = '.*Exception.*'
        str4 = '.*finished.*'
        Acount, Ccount, Ecount = 0, 0, 0

        for i in content:
            if re.match(str1,i):
                log.error("测试过程中出现了无响应，具体内容为："+i)
                aftfile.write(i)
                Acount+=1
            elif re.match(str2,i):
                log.error("测试过程中出现了奔溃，具体内容为："+i)
                aftfile.write(i)
                Ccount+=1
            elif re.match(str3,i):
                log.error("测试过程中出现了异常，具体内容为："+i)
                aftfile.write(i)
                Ecount+=1
        if Acount==0 or Ccount==0 or Ecount==0:
            for i in content:
                if re.match(str4,i):
                    log.info("测试正常完成")
                    aftfile.write(i)
        log.info("log分析结束")





