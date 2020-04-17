#To display the value at
def special(num):
    fib_list = [0,1]
    for i in range(2,num):
        fib_list.append(fib_list[i-2] + fib_list[i-1])
    return fib_list[num-1]

p=special(8)
print p
