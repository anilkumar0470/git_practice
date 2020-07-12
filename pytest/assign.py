
nums = input("enter nums seperated by comma") # "1,2,3"
if "," not in nums:
    print("the expected format is not wrong , ")


list = []
for i in nums:
    if i != ",":
        if i.isdigit():
            list.append(i)
        else:
            print("only digits are expected with comma seperated")


def func_to_check_ascening_order(new_list):
    #output_list = sorted(new_list) # 2 4 3 6
    output = []

    if new_list == output_list:
        return True
    else:
        return False
print(func_to_check_ascening_order(list))


#input 1,2,3
#1 2 3
# 1.2.3
#a b c
#1,2 3
