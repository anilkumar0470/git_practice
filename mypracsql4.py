#!/usr/bin/python
import MySQLdb
def emp_update_details(first_name,last_name,age,address,sex,income):
    #open database connection
    db = MySQLdb.connect("127.0.0.1","root","aneel","world")
    #prepare cursor object using cursor method()
    cursor = db.cursor()
    #cursor.execute("drop table if exists employee")
    #prepare sql query to insert a record into database
    sql = "insert into employee(first_name,last_name,age,address,sex,income)\
     values('%s','%s','%d','%s','%s','%f')" % \
    (first_name,last_name,age,address,sex,income)
    try:
        cursor.execute(sql)
        #after performing ddl operations we must use commit method to save the data
        db.commit()
    except:
        #to rollback the operation if any error occur it will rollback the operation
        db.rollback()
        #disconnecting from server
    db.close()

fd = open('emp1.txt','r')
#print ">>",fd.readlines()
for line in fd.readlines():
    l = line.split('|')
    #l = [anand,pithani,27,btm,m,10000]
    emp_update_details(l[0],l[1],int(l[2]),l[3],l[4],float(l[5]))
fd.close()