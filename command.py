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

log_path="/usr/src/log"
file_path="/usr/src/config"
img_path=os.getcwd()+"/img"
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
    #log.debug("start shutdown the adb service")
    kill_cmd = "adb kill-server"
    #log.info("the shutdown adb command is ：" + kill_cmd)
    os.popen(kill_cmd)

def adbstart():
    #log.debug("start the adb service")
    start_cmd = "adb start-server"
    #log.info("the start adb command is ：" + start_cmd)
    os.popen(start_cmd)

def adbcon(ip):
    #os.system("adb kill-server")
    log.debug("start to connect the devices，ip为:"+ip)
    con_cmd="adb connect %s"%(ip)
    #log.info("the connnect command is ：" + con_cmd)
    con_info=os.popen(con_cmd).read()
    #con_info=os.system(con_cmd)
    #print con_info.read()
    if "unable" in con_info:
        log.error("please check the ip and make sure you've install wireless")
        return False
    else:
        iscon=adbdev(ip)
        if "unauthorized" in iscon or "offline" in iscon:
            log.debug("reconnnect")
            adbcon(ip)
            #return False
        else:
            log.info("ip :"+ip+" is connected")
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
    check_cmd="adb devices|grep %s" %(ip)
    #log.info("check connection status commmand is  ："+  check_cmd)
    check_info=os.popen(check_cmd).read()
    print check_info
    #log.info("connect info is :"+check_info)
    return check_info

def adbmdev():
    check_cmd="adb devices"
    #log.info("check the connected devices command is ："+  check_cmd)
    check_info=os.popen(check_cmd)
    #log.info(check_info)
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
    log.info("get android version command is ："+  getversion_cmd)
    getversion_info=os.popen(getversion_cmd).read()
    log.info("android version is :"+getversion_info)
    return getversion_info.strip()

def adbgetpro(way,ip):
    getprono_cmd="adb  -s "+ phonecon(way,ip)+"  shell getprop ro.product.model"
    log.info("to get the device type command is ："+  getprono_cmd)
    getprono_info=os.popen(getprono_cmd).read()
    log.info("the device type is :"+getprono_info)
    return getprono_info.strip()

def adblogcat(way,ip,packageName):
    #tm=currnt time
    tm = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))
    print("start to collect the log")
    log.debug("start to collect the log")
    #define logname
    log_filename =log_path+"/"+ip+"#"+tm
    logcat_file = open(log_filename, 'w')
    #search the pid of packagename
    ps_cmd = "adb -s " + phonecon(way, ip) + "  shell ps|grep %s" % (packageName)
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
        log.info("packagename is  %s ,，can not get the pid" % (packageName))
        log_cmd = "adb -s "+ phonecon(way,ip)+"  logcat -v time"
        log.info("print all the logs command is ：" + log_cmd)
        log_info = subprocess.Popen(log_cmd, stdout=logcat_file, stderr=subprocess.PIPE)
        #print log_info
        time.sleep(10)
        log_info.terminate()
        print("device "+ip+" has complete print the log")
    else:
        log_cmd = "adb -s "+ phonecon(way,ip)+"  logcat -v time *:E |grep '%s' " % (str)
        log.info("print %s log command is ：" % (ip) + log_cmd)
        log_info = subprocess.Popen(log_cmd, stdout=logcat_file, stderr=subprocess.PIPE)
        #print log_info
        #time.sleep(10)
        log_info.wait()
        log_info.terminate()
        print("deivce " + ip + "log print has been finished")

def adbuninstall(way,ip,packageName):
    log.debug("check if "+ip+"is installed "+packageName)
    print("check if "+ip+"is installed "+packageName)
    find_cmd="adb -s "+ phonecon(way,ip)+"  shell pm list package|grep %s"%(packageName)
    log.info("the check command is ：" + find_cmd)
    print ("the check command is ：" + find_cmd)
    find_info=os.popen(find_cmd)
    length= len(find_info.read())
    #print len(find_info.read()), length <= 0
    if length <= 0 :
        log.info("device %s is nod installed %s"%(ip,packageName))
        print("device %s is not installed %s"%(ip,packageName))
    else:
        log.info("device %s is installed %s"%(ip,packageName))
        log.debug("start uninstalled the package")
        print("device %s is installed %s"%(ip,packageName))
        print("start uninstalled the package")
        uninstall_cmd="adb -s "+ phonecon(way,ip)+"  shell pm uninstall %s"%(packageName)
        log.info("the uninstall command is ：" + uninstall_cmd)
        print("the uninstall command is ：" + uninstall_cmd)
        uninstall_info=os.popen(uninstall_cmd)
        print uninstall_info.read()
        log.debug("uninstall complete")
        print("uninstall complete")

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
    log.debug("device "+ip+" is starting install "+name)
    print("device "+ip+" is starting install "+name)
    #install_cmd='adb -s "+ phonecon(way,ip)+"  shell pm install D:\python\\apk\%s'%(ip,name)
    install_cmd = "adb -s "+phonecon(way,ip)+" install -l -r %s/%s" % (file_path,name)
    #log.info("the install command is " + install_cmd)
    print("the install command is ：" + install_cmd)
    #install_info= subprocess.Popen(install_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    install_info=os.popen(install_cmd).read()
    #log.info("installing...")
    print("installing...")
    if "Success" in install_info:
        log.info("成功安装")
        return True
    #out=install_info.stdout.read()
    #err=install_info.stderr.read()
    #log.info(out)
    #print(out)
    #if err !="":
        #log.error(err)

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
    list_cmd = "tasklist |grep node"
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
    cpu_cmd = "adb  -s "+ phonecon(way,ip)+"  shell dumpsys cpuinfo|grep %s >%s/%s%s-cpu.txt" % (packageName,log_path,ip,tm)
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
    ps_cmd="adb -s "+ phonecon(way,ip)+"  shell ps|grep %s"%(packagename)
    log.info(ps_cmd)
    ps_info = os.popen(ps_cmd)
    uid=""
    for i in ps_info.readlines():
        log.info(i)
        uid_list = i.split()
        log.info(uid_list)
        uid = uid_list[0].replace("_","")
        log.info(uid)
    elec_cmd="adb -s "+ phonecon(way,ip)+"  shell dumpsys batterystats %s |grep %s"%(packagename,uid)
    log.info(elec_cmd)
    elec_info=os.popen(elec_cmd)
    log.info(elec_info.readline())

def texttodic(filename):
    log.debug("file to dict")
    print("file to dict")
    datafile = file_path+filename
    log.info(datafile)
    print(datafile)
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
        print(datafile + "is not exist!!!")
        log.error(datafile + "is not exist!!!")

def texttolist(filename):
    log.debug('file to list')
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
        log.error(datafile + "file is not exist")

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






