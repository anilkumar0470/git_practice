import datetime
import time
import re
def intial():
    e = {'Expiry Date': u'Sun Apr 05 00:55:58 PDT 2028'}
    i=convert(e)
    return i
def after():
    e = {'Expiry Date': u'Sun Apr 06 00:55:58 PDT 2029'}
    k=convert(e)
    return k

def convert(e):
    months = {"Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4, "May": 5, "Jun": 6, "Jul": 7, "Aug": 8, "Sep": 9, "Oct": 10,
              "Nov": 11, "Dec": 12}

    k = e['Expiry Date'].split(" ")
    hours=re.search("(\d\d):(\d\d):(\d\d)",e['Expiry Date']).group(1)
    minutess=re.search("(\d\d):(\d\d):(\d\d)",e['Expiry Date']).group(2)
    seconds=re.search("(\d\d):(\d\d):(\d\d)",e['Expiry Date']).group(3)
    d = datetime.datetime(int(k[5]), int(months[k[1]]), int(k[2]),int(hours),int(minutess),int(seconds))
    unixtime = time.mktime(d.timetuple())
    print(unixtime)
    return unixtime


i=intial()
k=after()
if k>i:
    print("pass")
else:
    print("fail")