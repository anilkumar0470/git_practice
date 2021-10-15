try:
    fd = open("aaa.txt","r")
except IOError:
    print("error :file not found")
else :
    l = fd.readlines()
    for i in l :
        print (i)
finally:
    print ("kkkkkk")



