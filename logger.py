# coding=utf-8
import logging
import os
import time
import sys

log_path="/usr/src/log"
if os.path.exists(log_path):
    pass
else:
    os.mkdir(log_path)

tm=time.strftime('%Y-%m-%d',time.localtime(time.time()))
logfile=log_path+"/"+tm+'-log.txt'

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s %(message)s',
                    filename =logfile,
                    filemode='a'
                    )
# 定义一个Handler打印INFO及以上级别的日志到sys.stderr
console = logging.StreamHandler(sys.stdout)
console.setLevel(logging.ERROR)
# 设置日志打印格式
formatter = logging.Formatter('%(levelname)-8s：%(message)s')
console.setFormatter(formatter)
# 将定义好的console日志handler添加到root logger
logging.getLogger('').addHandler(console)
def info(msg):
    logging.info(msg)
def debug(msg):
    logging.debug(msg)
def error(msg):
    logging.error(msg)
    sys.stderr.write(msg)
    sys.stderr.write('\n')
    raise Exception(msg)

    #sys.stderr.writelines(msg)
    #sys.stderr.write(msg)
