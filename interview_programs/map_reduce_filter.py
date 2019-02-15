def add(num):
    return num + num

a = map(add, [1,2,2])
print(type(a))
print(list(a))