# -*- coding: utf-8 -*-
from multiprocessing import Process,Pool
import command as cmd
import jkh_test as test
#import sjd_test as test
import logger as log
import time

def func(way,ip,port,apkname,packageName):
    try:
        for i in range(1,21):
            print "%s安装了%d次"%(ip,i)
        #卸载app
            cmd.adbuninstall(way,ip, packageName)
        #安装app
            cmd.adbinstall(way,ip, apkname)
            time.sleep(3)

        #启动appium
        #cmd.startappium(ip,port)
        #执行appium脚本
        test.ip = ip
        log.info(ip)
        test.port = port
        log.info(port)
        test.apkname=apkname
        log.info(apkname)
        test.packageName=packageName
        log.info(packageName)
        #for i in range(2):
        #test.run(ip)
        #cmd.adbmonkey(way,ip,packageName,100)

    except Exception as e:
        print  e
    finally:
        #cmd.adbmeninfo(way,ip,packageName)
        #cmd.adbcpuinfo(way,ip,packageName)
        #获取logcat日志
        cmd.adblogcat(way,ip, packageName)
    print "执行完成"

def main():
    #检查相关文件路径
    #cmd.checkpath()
    #杀appium进程
    #cmd.killappium()
    #cmd.killadb()
    #杀adb进程
    #cmd.adbkill()
    #启动adb服务
    cmd.adbstart()
    #获取配置文件信息
    dics=cmd.texttodic("\\config.txt")
    key=dics.keys()
    log.info(key)
    dic=dics[key[0]]
    log.info(dic)
    svnpath=dic['svnpath']
    packageName = dic['packagename']
    log.info(packageName)
    activity = dic['activity']
    log.info(activity)
    name = dic['apkname']
    log.info(name)
    way = dic['way']
    port = dic['port']
    # 检查svn，判断是否通过svn安卓
    apkname=cmd.svncheck(svnpath)
    # svn有更新，对已经获取到的name重赋值
    if apkname is not None:
        name=apkname
    pool = Pool(processes=5)
    ipfile="\\ip.txt"
    #way=1 通过wifi连接设备
    if way=="1":
        for ips in cmd.texttolist(ipfile):
            ip=ips.strip()
            cmd.adbcon(ip)
            '''
            p = Process(target=func, args=(way,ip,port,name,packageName,))
            p.start()
            port = int(port) + 2
            time.sleep(3)
            '''
            pool.apply_async(func, (way,ip, port, name, packageName,))
            port = int(port) + 2
        pool.close()
        pool.join()
    else:
        #way=3 wifi和usb混合连接
        if way=="3":
            for ips in cmd.texttolist(ipfile):
                ips = ips.strip()
                cmd.adbcon(ips)
        for ip in cmd.adbmdev():
            log.debug(ip)
            if "List" in ip.strip():
                pass
            elif ip.strip() == "":
                pass
            else:
                ip = ip.strip().split("device")[0].strip()
                if ":5555" in ip:
                    ip = ip.strip().split(":5555")[0]
                log.info( ip)
                '''
                p = Process(target=func, args=(way, ip, port, name, packageName,))
                p.start()
                port = int(port) + 2
                time.sleep(3)
                '''
                pool.apply_async(func, (way,ip, port, name, packageName,))
                port = int(port) + 2
        pool.close()
        pool.join()

if __name__ == "__main__":
    main()
