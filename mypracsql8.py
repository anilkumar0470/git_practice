import MySQLdb
db = MySQLdb.connect("127.0.0.1","root","aneel","world")
cursor = db.cursor()
cursor.execute("select version()")
#fetch a single row using fetchone() method
data = cursor.fetchone()
print "database version : %s" % data
#disconnect from  server
db.close()