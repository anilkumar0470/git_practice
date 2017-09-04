import time
#ctime is a method in time moduleto see  the current time
print time.ctime()
#time is a method in time module and it will generate number
print time.time()
#localtime is method to generate something
#time.struct_time(tm_year=2016, tm_mon=3, tm_mday=3, tm_hour=19, tm_min=56, tm_sec=34, tm_wday=3, tm_yday=63, tm_isdst=0)
print time.localtime(time.time())
print time.localtime()
time.sleep(5)
# sleep is a method to stop the execution up to 5 seconds
#the below program is to add 15 seconds to current time
print "the time is :",time.ctime()
later = time.time() + 15
print "15 sec from now :",time.ctime(later)
#output of above program
#the time is : Thu Mar 03 20:03:07 2016
#15 sec from now : Thu Mar 03 20:03:22 2016
#strptime is a  method to return output as tuple by taking argument
#asctime()
now = time.ctime()
print now
parsed = time.strptime(now)
print ">>",parsed
print "---",time.strftime("%a %b %d %H %M %S %Y",parsed)
"""
Thu Mar 03 20:11:58 2016
>> time.struct_time(tm_year=2016, tm_mon=3, tm_mday=3, tm_hour=20, tm_min=11, tm_sec=58, tm_wday=3, tm_yday=63, tm_isdst=-1)
--- Thu Mar 03 20 11 58 2016
"""