#coding=utf-8
import MySQLdb
import datetime
import logger as log
class mysql():
    def __init__(self):
        self.db = MySQLdb.connect(
            host='10.167.200.58',
            port=3306,
            user='creditor',
            passwd='creditor',
            db='mobileloan', )

    def valicode(self):
        log.debug('操作数据库')
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()
        code=''
        #查找用户id
        cus_idsql="select code from muser_validcode order by create_time DESC LIMIT 0, 1"
        log.info( cus_idsql)
        try:
            # 执行SQL语句
            cursor.execute(cus_idsql)
            # 获取所有记录列表
            results = cursor.fetchall()
            log.info( results)
            for row in results:
                code= row[0]
        except:
            log.info( "获取不到数据")
        return code

    def selectcusid(self,username):
        log.debug('操作数据库')
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()
        cus_id=''
        #查找用户id
        cus_idsql="select id from muser_info where username='%s'"%(username)
        log.info( cus_idsql)
        try:
            # 执行SQL语句
            cursor.execute(cus_idsql)
            # 获取所有记录列表
            results = cursor.fetchall()
            log.info( results)
            for row in results:
                cus_id= row[0]
        except:
            log.info( "获取不到数据")
        return cus_id

    def select(self,cus_id):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()
        # SQL 查询语句
        sql = "SELECT loan_day FROM loan_info where customer_id='%s' and status='3'" % (cus_id)
        log.info( sql)
        # sql = "SELECT * FROM loan_info"
        try:
            # 执行SQL语句
            cursor.execute(sql)
            # 获取所有记录列表
            results = cursor.fetchall()
            for row in results:
                time=row[0]
                '''
                loan_time = row[0]
                repay_time = row[1]
                time = (repay_time - loan_time).days
                log.info( time)
                log.info( row)
                '''
                log.info(time)
        except:
            log.info( "获取不到数据")

        return time

    def normalupdate(self,username):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()
        cus_id = self.selectcusid(username)
        time=self.select(cus_id)

        no=datetime.datetime.now()
        now = no.strftime("%Y-%m-%d %H:%M:%S")
        log.info( now)
        loan = no + datetime.timedelta(-time+1)
        loan_time = loan.strftime("%Y-%m-%d %H:%M:%S")
        log.info( loan_time)
        update_sql="update loan_info set plan_repay_time='%s',loan_time='%s' where customer_id='%s'"%(now,loan_time,cus_id)
        log.info( update_sql)
        try:
            # 执行SQL语句
            cursor.execute(update_sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        # 关闭数据库连接
        self.db.close()


    def earlyupdate(self,username):
        # 使用cursor()方法获取操作游标
        cursor = self.db.cursor()
        cus_id = self.selectcusid(username)
        time = self.select(cus_id)

        no = datetime.datetime.now()
        now = no.strftime("%Y-%m-%d %H:%M:%S")
        log.info(now)
        plan=no+datetime.timedelta(1)
        plan_time=plan.strftime("%Y-%m-%d %H:%M:%S")
        log.info(plan_time)
        loan = no + datetime.timedelta(-time+2)
        loan_time = loan.strftime("%Y-%m-%d %H:%M:%S")
        log.info( loan_time)
        update_sql = "update loan_info set plan_repay_time='%s',loan_time='%s' where customer_id='%s'" % (
        plan_time, loan_time, cus_id)
        log.info( update_sql)
        try:
            # 执行SQL语句
            cursor.execute(update_sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 发生错误时回滚
            self.db.rollback()
        # 关闭数据库连接
        self.db.close()

if __name__ == '__main__':
    username='13883000000'
    sql=mysql()
    #sql.selectdata(username)
    sql.normalupdate(username)