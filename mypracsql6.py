import MySQLdb
db = MySQLdb.connect("127.0.0.1","root","aneel","world")
cursor = db.cursor()
sql = "delete from employee where age = %d" % (27)
try:
    #excute the sql command
    print "==>",sql
    cursor.execute(sql)
    db.commit()
except :
    print "hellooo"
    db.rollback()
db.close()