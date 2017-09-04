d = input("enter the date like 01 or 11")
m = input("enter the month")
y = input("enter year ")
global od,od1,od2,od3,od4

print y  #1993
yy = y - 1
print yy #1992
if yy > 400:
    y1 = yy % 400
    print y1 #392
    y11 = yy - y1
    print y11 #1600
    if y1 >100:
        y2 = y1%100
        print y2#92
        y22 = y1 - y2
        print y22#300
        y4 = y22 %100
        if y4==1:
            od4 = 5
        elif y4 == 2:
            od4 = 3
        else :
            od4 = 1
        y23 = y2/4
        print y23
        y24 = y23 + y2
        print y24
        od3 = y24 % 7# may be final output
        print od3
    else :
        od4 = 0
        y3 = y1/4
        print y3
        y31 = y3 + y1
        print y31
        od3 = y31 % 7
        print od3 # may be final output
elif yy >100:
        y2 = yy%100
        print y2#92
        y22 = yy - y2
        print y22#300
        y4 = y22%100
        if y4==1:
            od4 = 5
        elif y4 == 2:
            od4 = 3
        else :
            od4 = 1
        y23 = y2/4
        print y23
        y24 = y23 + y2
        print y24
        od3 = y24 % 7# may be final output
        print od3
else :
    y3 = yy/4
    print y3
    y31 = y3 + yy
    print y31
    od3 = y31 % 7
    print od3 # may be final output
if y%4 ==0:
    if m >= 3:
        od2 = 1
    else :
        od2 = 0
else :
    od2 = 0

#d = 12
#m = 07


if m <= 12:
    mm = m - 1
    if mm ==0:
        od = 0 +d
        print od
    elif mm == 1:
        od =31+d
        print od
    elif mm == 2:
        od =59 + d
        print od
    elif mm == 3:
        od = 90 + d
        print od
    elif mm == 4:
        od = 120 +d
        print od
    elif mm == 5:
        od =151+d
        print od
    elif mm == 6:
        od =181 + d
        print od
    elif mm == 7:
        od = 212 + d
        print od
    elif mm == 8:
        od = 243 +d
        print od
    elif mm == 9:
        od =273+d
        print od
    elif mm == 10:
        od =304 + d
        print od
    else:
        od = 334 + d
        print od
else:
    print "enter the month lessthan 13"

o1= od +  od2 + od3 + od4
odd = o1%7
if odd == 0:
    print "may be it is sunday"
elif odd == 1:
    print "may be monday"
elif odd == 2:
    print "may be tuesday"
elif odd == 3:
    print "may be wednesday"
elif odd == 4:
    print "may be thursday"
elif odd == 5:
    print "may be friday"
else:
    print "it's saturday"
print "final:",odd