import MySQLdb
global db
global cursor
db = MySQLdb.connect("localhost","root","aneel","world")
cursor = db.cursor()


def update_details(age,income):
    sql = "update employee set age = %d where income >= %d"%(age,income)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
update_details(30,5000)
db.close()