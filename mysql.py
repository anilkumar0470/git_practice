import MySQLdb
db = MySQLdb.connect("localhost","root","aneel","world")
cursor = db.cursor()
sql = "select version()"
cursor.execute(sql)
db.close()