try:
    f = open("test1.txt","r")
    s = f.readline()
    print "s==>",s,"type:",type(s)
    i = int(s.strip())
    print "type:",type(i),"----",i
except (IOError,ValueError):
    print "opps got exception"
except:
    print "unexcepted error:"
finally:
    try:
        f.close()
    except NameError:
        print "opps its not defined"
    print "i am closing file"