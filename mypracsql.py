#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect("127.0.0.1","root","aneel","world")
cursor = db.cursor();
#cursor.execute("drop table if exists employee")
sql = """create table if not exists employee4(
         first_name char(20) not null,
         last_name char(20),
         age int,
         address char(20),
         sex char(1),
         income float)"""
cursor.execute(sql)
sql1 = """show databases"""
cursor.execute(sql1)
db.close()