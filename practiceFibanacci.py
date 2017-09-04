

def special(num):
    print "hai"
    a = 0# 0
    print a # 0
    b = 1
    for i in range(num):
        c = a + b#1 1 2 3 5 8 13 21
        print c#1 1 2 3 5 8 13 21
        b = a# 0 1 1 2 3 5 8  13
        a = c# 1 1 2 3 5 8 13 21
d = input("enter a value ")
num = d
special(num)