#!/usr/bin/python
import MySQLdb
db = MySQLdb.connect("127.0.0.1","root","aneel","world")
cursor = db.cursor();
#cursor.execute("drop table if exists employee")
sql = """insert into employee(first_name,last_name,age,address,sex,income) values('anilkumar','pathapati',22,'silkboard','m',10000)"""
try:
    cursor.execute(sql)
    #after performing ddl operations we must use commit method to save the data
    db.commit()
except:
    #to rollback the operation if any error occur it will rollback the operation
    db.rollback()
#disconnecting from server
db.close()