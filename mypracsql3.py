#!/usr/bin/python
fname = raw_input("enter first name ")
lname = raw_input("enter last name")
age = input("enter age")
address = raw_input("enter address")
sex = raw_input("enter m or f")
income = input("enter income")
import MySQLdb
db = MySQLdb.connect("127.0.0.1","root","aneel","world")
cursor = db.cursor();
#cursor.execute("drop table if exists employee")
#sql = """insert into employee(first_name,last_name,age,address,sex,income) values('anilkumar','pathapati',22,'silkboard','m',10000)"""
#sql= "insert into employee(first_name,last_name,age,address,sex,income) values( '%s','%s','%d','%s','%s','%f')" %('bunny','gorepati',21,'btm','m',5000)
sql= "insert into employee(first_name,last_name,age,address,sex,income)\
 values( '%s','%s','%d','%s','%s','%f')"\
    %(fname,lname,age,address,sex,income)

cursor.execute(sql)
    #after performing ddl operations we must use commit method to save the data
db.commit()
#to rollback the operation if any error occur it will rollback the operation
#disconnecting from server
db.close()