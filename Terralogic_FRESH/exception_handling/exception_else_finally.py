try :
    fd = open("aaaa.txt","r")
except IOError:
    print "error :file not found"
else :
    l = fd.readlines()
    for i in l :
        print i
finally:
    print "Read DoNe"
