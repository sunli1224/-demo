#coding:utf-8
import MySQLdb
class mysqlConnect:
    def __init__(self):
        self.connect = MySQLdb.connect(user='root', db='dishesdemo', passwd='s19961224l', host='localhost',
                        charset='utf8')


    def search_data(self, sql):#查询语句
        db = self.connect.cursor()
        db.execute(sql)
        result = db.fetchall()
        self.connect.commit()
        db.close()
        return result

    def find_data(self,sql):#更新语句
        db = self.connect.cursor()
        db.execute(sql)
        # result = db.fetchall()
        self.connect.commit()
        db.close()
        # return result

