import pymysql


dbinfo = {
    "host": "49.235.92.12",
    "user": "root",
    "password": "123456",
    "port": 3309}


class DbConnect():
    def __init__(self, db_cof, database=""):
        self.db_cof = db_cof
        # 打开数据库连接
        self.db = pymysql.connect(database=database,
                                  cursorclass=pymysql.cursors.DictCursor,
                                  **db_cof)

        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()

    def select(self, sql):
        # SQL 查询语句
        # sql = "SELECT * FROM EMPLOYEE \
        #        WHERE INCOME > %s" % (1000)
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def execute(self, sql):
        # SQL 删除、提交、修改语句
        # sql = "DELETE FROM EMPLOYEE WHERE AGE > %s" % (20)
        try:
           # 执行SQL语句
           self.cursor.execute(sql)
           # 提交修改
           self.db.commit()
        except:
           # 发生错误时回滚
           self.db.rollback()

    def close(self):
        # 关闭连接
        self.db.close()


def select_sql(sql, db_cof=dbinfo, dbname="djangoweb"):
    '''SQL查询函数'''
    db = DbConnect(db_cof, dbname)
    result = db.select(sql)  # 查询
    db.close()
    return result


def execute_sql(sql, db_cof=dbinfo, dbname="djangoweb"):
    '''SQL提交函数'''
    db = DbConnect(db_cof, dbname)
    db.execute(sql)  # 查询
    db.close()


if __name__ == '__main__':
    sql = "SELECT count(*) FROM `hello_articleclassify` WHERE n = '技术类';"
    a = select_sql(sql)
    print(a)

