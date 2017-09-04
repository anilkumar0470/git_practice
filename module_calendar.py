import calendar
#print calendar.calendar(2016)
#calender is a method to produce calender of that year
#c = calendar.TextCalendar(calendar.MONDAY)
#if we specifiy monday then it will give output as starting day as monday
c = calendar.TextCalendar(calendar.SUNDAY)
#print ">>",c.pryear(2016)
#pryear is for printing is entire year
print c.prmonth(2016,10)