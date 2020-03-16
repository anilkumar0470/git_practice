# def sample():
#     try :
#         print(50/0)
#     except:
#         raise Exception
# try:
#     sample()
# except:
#     print("sss")

# result = [i*3 if i%2 == 0  else i*2 for i in range(10) ]
# print(result)
#
# data = {"day":["1/2/21","2/2/22"],}

import time

def sample(k):
        print(k)
start_time = time.time()
for k in range(10000000):
    sample(k)
end_time = time.time()

func = lambda a  : print(a)
sstime = time.time()

for i in range(10000000):
    func(i)
etime = time.time()
print(end_time-start_time)
print(etime - sstime)




# def fun():
#     print("hello")
#
# x= lambda:print("hello")

# def test(a):
#     start=time.time()
#     for p in range(10000000):
#         a()
#     end=time.time()
#     return(start-end)
# print(test(x)-test(fun))



