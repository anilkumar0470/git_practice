# try :
#     fd = open("aaaa.txt","r")
# except IOError:
#     print "error :file not found"
# else :
#     l = fd.readlines()
#     for i in l :
#         print i
# finally:
#     print "Read DoNe"

q = 10
try :
    print(q)
except NameError:
    pass
else:
    print("else block")
finally:
    print("finally block")