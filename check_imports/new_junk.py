# import hello
# s = hello.sample1
# del hello
# print()


#
# fd1 = open("hello.txt")
# fd2 = open("file2.txt", "a+")
#
# data1 = fd1.readlines()
# data2 = fd2.readlines()
# fd2.close()
# fd3 = open("file2.txt", "a")
# for state in data1:
#     if state + "\n" not in data2:
#         fd3.write(state.strip()+"\n")
#
#
#     else:
#         pass
#
# fd1.close()
# fd3.close()
#
#
#
# {
#   "array": [5, 1, 22, 25, 6, -1, 8, 10],
#   "sequence": [5, 1, 25, 22, 6, -1, 8, 10]
# }
# 5, 1, 22, 25, 6, -1, 8, 10
# 5, 1, 22, 25, 6, -1, 8, 10, 12

array = [5, 1, 22, 25, 6, -1, 8, 10]
sequence = [ 1, 6, -1, 10]


def isValidSubsequence(array, sequence):
    # Write your code here.
    previous_index = 0
    current_index = None
    for num in sequence:
        if num in array:
            current_index = array.index(num)
            if num not in array:
                return False
            else:
                if previous_index:
                    if current_index < previous_index:
                        return False
                else:
                    previous_index = current_index
                array.remove(num)
        else:
            return False
    else:
        return True
    # for value in array:
    #     if previous_index == len(sequence):
    #         break
    #     if sequence[previous_index] == value:
    #         previous_index += 1
    # return previous_index == len(sequence)
    
# result = isValidSubsequence(array, sequence)
# print(result)


def sum_of_k_value():
    array = [1,3,7]
    k = 6
    array.sort()
    for number in array:
        if k - number in array:
            pass
        else:
            return False
        return True
print(sum_of_k_value())