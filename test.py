# -*- coding: utf-8 -*-
'''
import command as cmd
if __name__ == '__main__':
    ip = '10.167.160.92'
    packageName = 'com.djr.zichanjia'
    try:
        print "begin"
        cmd.adbcon(ip)
        cmd.adbmonkey(ip, packageName,'1000')
    except Exception as e:
        print  e
    finally:
        #获取logcat日志
        cmd.adblogcat(ip, packageName)
    print "执行完成"

import random
if __name__ == '__main__':
    x=1920
    print random.randint(20, 1920)

import  StringIO
import newzichanjia
if __name__ == '__main__':
    ip='10.167.160.60'
    port='4723'
    apkname='zichanjia15.apk'
    test = newzichanjia.zichanjia(ip, port,apkname)
    test.stat_appium()
    test.test_brows()
    test.test_login()

import command as cmd
import os
def txttodic(filename):
    datafile = cmd.file_path + "\\" + filename
    if os.path.exists(datafile):
        f = open(datafile)
        dic=dict()
        key = ""
        lines = f.readlines()
        for l in lines:
            if l.startswith('#'):
                key = l.strip('\n').strip('#').lower()
            else:
                line = l.strip().split(':')
                if key in dic:
                    dic[key].update({line[0].lower(): line[1]})
                else:
                    dic.update({key: {line[0].lower(): line[1]}})

        return dic
    else:
        print datafile + "文件不存在"


if __name__ == '__main__':
    filename='10.167.170.35data.txt'
    aa=txttodic(filename)
    print aa.get('phone2')
    #print aa['phone1']
    print aa.has_key('phone3')
    key=aa.keys()
    print key
    print len(key)
    adbcmd='adb -d shell getprop ro.product.model'
    getprono = os.popen(adbcmd).read()
    a=getprono.strip().lower()
    print a
    if aa.has_key(a):
        c=aa[a]
        print c
    else:
        c=aa[key[0]]
        print c
    print 'ok'


import sys
import threading
import Queue
q = Queue.Queue()
def worker1(x, y):
	func_name = sys._getframe().f_code.co_name
	print "%s run ..." % func_name
	q.put((x + y, func_name))
def worker2(x, y):
	func_name = sys._getframe().f_code.co_name
	print "%s run ...." % func_name
	q.put((x - y, func_name))

def worker(x, y):
	func_name = sys._getframe().f_code.co_name
	print "%s run ...." % func_name
	q.put((x - y, func_name))
if __name__ == '__main__':
	result = list()
	t1 = threading.Thread(target=worker1, name='thread1', args=(10, 5, ))
	t2 = threading.Thread(target=worker2, name='thread2', args=(20, 1, ))
	print '-' * 50
	t1.start()
	t2.start()
	t1.join()
	t2.join()
	while not q.empty():
		result.append(q.get())
        print result
	for item in result:
		if item[1] == worker1.__name__:
			print "%s 's return value is : %s" % (item[1], item[0])
		elif item[1] == worker2.__name__:
			print "%s 's return value is : %s" % (item[1], item[0])




# coding:utf-8
import threading
import time
import Queue
import sys
q = Queue.Queue()
#方法一：将要执行的方法作为参数传给Thread的构造方法
def action(arg):
    time.sleep(1)
    #print 'the arg is:%s\r' %arg
    func_name = sys._getframe().f_code.co_name
    print "%s run ...." % func_name
    q.put((arg, func_name))

for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    t.start()
    t.join()
    result = list()
    while not q.empty():
        result.append(q.get())
        #print result
        for item in result:
            print "%s 's return value is : %s" % (item[1], item[0])

print 'main thread end!'




#coding:utf-8
import threading
import time
import Queue
import sys
q = Queue.Queue()
result = list()
def action(arg):
    time.sleep(arg*10)
    func_name = sys._getframe().f_code.co_name
    print  'sub thread start!the thread name is:%s    ' % threading.currentThread().getName()
    print 'the arg is:%s   ' %arg
    time.sleep(1)
    q.put((arg, func_name))

thread_list = []    #线程存放列表
for i in xrange(4):
    t =threading.Thread(target=action,args=(i,))
    #t.setDaemon(True)
    thread_list.append(t)


for t in thread_list:
    t.start()

for t in thread_list:
    t.join()
    while not q.empty():
        result.append(q.get())
print result

for item in result:
    print "%s 's return value is : %s" % (item[1], item[0])

import random
if __name__ == '__main__':
    a=('qwe','123','HUJB')
    print random.choice(a)



# coding=utf-8
import subprocess
import time
import command as cmd

packageName='com.xihe.moblie.credit'

fo = open(r"D:\foo.txt", "w")
# 获取进程ID
getProcessIdcmd = 'adb shell ps | grep %s'% (packageName)
print getProcessIdcmd
p = subprocess.Popen(getProcessIdcmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
content = p.stdout.readlines()
print content
print len(content)
if len(content) >= 1:
    processId = content[0].split()[1]
    print processId
else:
    print "not get processID"
# 获取进程对应的UID
getUidcmd = 'adb shell cat /proc/' + processId + '/status | grep Uid'
print getUidcmd
p = subprocess.Popen(getUidcmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
content = p.stdout.readlines()
print content
uidList = content[0].strip().split('\t')
print uidList
uid = uidList[1]

# 获取UID对应的Traffic
getTrafficcmd = 'adb shell cat /proc/net/xt_qtaguid/stats | grep ' + uid

for i in range(10):
    currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    traffic_initial = [0] * 16
    traffic_prefix = []
    p = subprocess.Popen(getTrafficcmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for line in p.stdout.readlines():
        ll = line.strip()
        ll2 = ll.replace(' ', ',')
        ll2_list = ll2.split(',')
        traffic_list = ll2_list[5:]
        traffic_prefix = ll2_list[0:4]
        traffic_list_int = [int(e) for e in traffic_list]

        traffic_initial = [x + y for x, y in zip(traffic_initial, traffic_list_int)]
        # print traffic_list
        print currentTime + "," + ll2
    retval = p.wait()
    print traffic_initial
    traffic_list_str = [str(e) for e in traffic_initial]
    print traffic_prefix + traffic_list_str
    traffic = ','.join(traffic_prefix + traffic_list_str)
    print currentTime + ',' + traffic
    fo.write(currentTime + ',' + traffic + '\n')

    time.sleep(60)
    print '--------------'
fo.close()


import command as cmd
import subprocess
import os
if __name__ == '__main__':
    packageName="com.xihe.moblie.credit"
    ps_cmd = "adb  shell ps|findstr %s" % (packageName)
    print ps_cmd
    ps_info =os.popen(ps_cmd)
    str = " "
    for i in ps_info.readlines():
        pid_list = i.split()
        print pid_list
        pid = pid_list[0]
        print pid
        str = str+ " " + pid
    print str

'''
# encoding: UTF-8
str=input("请输入：")
print  str















