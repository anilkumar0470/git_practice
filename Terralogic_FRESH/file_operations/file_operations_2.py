fd = open("zzz.txt","r")
print("after opening")
print(fd.tell())
print(fd.read(200))
print("after reading content 10")
print(fd.tell())
print("moving the cusror to starting postion")
fd.seek(0,0)
print(fd.tell())
print("moving the cusror to ending postion")
fd.seek(0,2)
print(fd.tell())






# lines = fd.readlines()
# print(type(lines))
# for line in lines:
#     print(line)
# content = fd.read()
# print(type(content))
# lines = content.split("\n")
# for line in lines:
#     print(line)
# tell() -- postion of the cursor



#seek(0,0) # seeking
#seek(0,1)
#seek(0,2)

fd.close()
