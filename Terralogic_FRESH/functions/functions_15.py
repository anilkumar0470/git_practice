# *args **kwargs
# *args tuple
def std_dict(name,*marks,**std_dict1):
    print(marks)
    print(std_dict1)
    print ("="*50)
    # =====================================================
    print  ("student details")
    print ("="*20)
    print ("Name is  :",name)
    f = True
    total = 0
    for i in marks: # 95,99,99,95,100
        total += i # total = total + i # 95 + 0
        if i < 35:
            f = False
    # True or False
    if f == True:
        print ("........!!!!!!Congratulations!!!!!!!......")
        result = "pass"
        print ("result:",result)
    else :
        result = "fail"
        print ("result:",result)
        print ("@@@Better luck next time@@@")
    print ("total marks :",total)
    for k,v in std_dict1.items():
        print (k,"-",v)
# std_dict("kumar.p",95,9,99,95,100,age = 22,loc = "hyderabad",mobile=3434)


#
# a = 0
# print (a)
# b = 1
# for i in range(10):
#     c = a + b # 1 1 2
#     print (c)
#     b = a # 0  1  1
#     a = c # 1  1  2   2


def fibonacci_series(num):
    a = 0
    print(a)
    b = 1
    for i in range(num):
        c = a + b  # 1 1 2
        print(c)
        b = a  # 0  1  1
        a = c  # 1  1  2   2
# fibonacci_series(2)


# return keyword


def addition_of_numbers(a,b):
    result = a + b
    return result

def dispaly_result():

    return  "something"



def another_function():
    result_var  = dispaly_result()
    a = addition_of_numbers(10, 20)

    print(result_var, a)

