try :
    fd = open("aaa.txt","r")
except IOError:
    print "error :file not found"
else :
    l = fd.readlines()
    for i in l :
        print i
finally:
    try :

        if not fd.closed:
            fd.close()
    except NameError:
        print "its not defined"
    print "Read DoNe"
