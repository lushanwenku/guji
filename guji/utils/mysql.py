import pymysql

from guji.utils.config import *


class MySQL():
    def __init__(self, host=MYSQL_HOST, username=MYSQL_USER, password=MYSQL_PASSWORD, port=MYSQL_PORT,
                 database=MYSQL_DATABASE):
        """
        MySQL初始化
        :param host:
        :param username:
        :param password:
        :param port:
        :param database:
        """
        try:
            self.db = pymysql.connect(host, username, password, database, charset='utf8', port=port)
            self.cursor = self.db.cursor()
        except pymysql.MySQLError as e:
            print(e.args)

    #关闭链接
    def close(self):
        self.cursor.close()
        self.db.close()


    def insert(self, table, data):
        """
        插入数据
        :param table:
        :param data:
        :return:
        """
        insert_id = 0
        keys = ', '.join(data.keys())
        values = ', '.join(['%s'] * len(data))
        sql_query = 'insert into %s (%s) values (%s)' % (table, keys, values)
        try:
            self.cursor.execute(sql_query, tuple(data.values()))
            insert_id = self.cursor.lastrowid
            self.db.commit()
            #self.close()
        except pymysql.MySQLError as e:
            print(e.args)
            self.db.rollback()
        return insert_id

    #查询单行记录
    def get_one(self,sql):
        res = None
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchone()
        except pymysql.MySQLError as e:
            print("查询失败!")
            print(e.args)
        return res

    #查询列表数据
    def get_all(self,sql):
        res = None
        try:
            self.cursor.execute(sql)
            res = self.cursor.fetchall()
            self.close()
        except pymysql.MySQLError as e:
            print(e.args)
            print("查询失败！")
        return res

    #插入数据
    def insert_sql(self,sql):
        count = 0
        insert_id = 0
        try:
            count = self.cursor.execute(sql)
            insert_id = self.cursor.lastrowid
            self.db.commit()
            #self.close()
        except pymysql.MySQLError as e:
            print("操作失败！")
            print(e.args)
            self.db.rollback()
        #return count
        return insert_id

    #修改数据
    def edit(self,sql):
        return self.__insert(sql)

    #删除数据
    def delete(self,sql):
        return self.__insert(sql)

    #更新数据
    def update(self,sql):
        return self.__insert(sql)

# if __name__ == '__main__':
#     data = {'hello':1,'good':2,'boy':3,'doiido':4}
#     print(tuple(data.keys()))
#     print(tuple(data.values()))
