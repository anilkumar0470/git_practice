
def bubble_sort(list):
    for num in range(len(list)-1, 0, -1):
        for index in range(num):
            if list[index] > list[index + 1]:
                temp = list[index]
                list[index] = list[index + 1]
                list[index + 1] = temp
list = [-2, 45, 0, 11, -9]
bubble_sort(list)
print(list)