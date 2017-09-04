import os
import time

print "current directory:",os.getcwd()
scriptPath = os.getcwd()

print "make directory:",os.mkdir("newdir")
os.chdir("./newdir")
time.sleep(5)
fd = open("input.txt","w")
fd.close()
print "remove file :",os.remove("input.txt")
time.sleep(5)
os.chdir("..")
time.sleep(5)
print "remove directory:",os.rmdir("newdir")
time.sleep(5)
print "change the directory:",os.chdir("D://ANIL KUMAR")
time.sleep(5)
print "coming back to scriprts:",os.chdir(scriptPath)
time.sleep(5)
print "script path we are:",os.getcwd()