import MySQLdb
db = MySQLdb.connect("127.0.0.1","root","aneel","world")
cursor = db.cursor()
# prepare sql query to fetch data from the database
sql = "select * from employee where income >= %d " %(2000)
try:
    #excute the sql command
    print "==>",sql
    cursor.execute(sql)
    #fetch all the rows in alist of lists
    results = cursor.fetchall()
    print "===",results
    for row in results:
        print "---",row
        first_name = row[0]
        last_name = row[1]
        age = row[2]
        address = row[3]
        sex = row[4]
        income = row[5]
        # now print fetched result
        print "%s %s %d %s %s %f" % \
              (first_name,last_name,age,address,sex,income)
except :
    print "error : unable to fetch data"
#disconnect from server
db.close()