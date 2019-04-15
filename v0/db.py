#!/usr/bin/python
#_*_coding:utf-8_*_

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import datetime
import MySQLdb
import time

import conf

class DB():
    def __init__(self):
        try:
            host = conf.dbhost
            port = conf.dbport
            user = conf.dbuser
            passwd = conf.dbpassword

            dbname = conf.dbname
            charset = 'utf8mb4'
            self.conn = MySQLdb.connect(host=host, user=user, passwd=passwd, db=dbname, port=int(port),
                                        charset=charset, autocommit=True)
            self.cur = self.conn.cursor()
        except Exception as e:
            print str(e)

    def execute(self, sql):
        try:
            lines = self.cur.execute(sql)
            return lines, self.cur.fetchall()
        except Exception as e:
            print str(e)
            self.__init__()
            return (0, ((),))

    def commit(self):
        try:
            self.conn.commit()
        except Exception as e:
            print str(e)
            self.__init__()

    def __del__(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception as e:
            print str(e)


def main():
    db = DB()
    print db.execute("show tables;")
    print db.execute("select * from wpdatabase.wp_users")


if __name__ == "__main__":
    main()
