# palindrome
def verify_palindrome_of_number(num1):
    res = ""
    for i in str(num1):
        res = i + res

    if res == str(num1):
        print(f"given number {num1} is palindrome")
    else:
        print(f"given number {num1} is not palindrome")


verify_palindrome_of_number(123)
verify_palindrome_of_number(12121)

def verify_palindrome_of_string(input_str):
    res1 = ""
    for i in input_str:
        res1 = i + res1
    if res1 == input_str:
        print(f"given string {input_str} is palindrome")
    else:
        print(f"given string {input_str} is not palindrome")


# verify_palindrome_of_string("anil")
# verify_palindrome_of_string("ababa")

def display_ip_from_given_network(ip_address):
    out = ip_address.split(".")
    if int(out[-1]) < 155:
        for i in range(100):
            var1 = ".".join(out[:3])
            out1 = f"{var1}.{i}"
            print(out1)
    elif int(out[-1]) < 254:
        third = int(out[-2]) + 1
        for i in range(100):
            var2 = ".".join(out[:2]) + f".{third}.{i}"
            print(var2)


# display_ip_from_given_network("10.10.10.157")

def remove_file_using_python(file_path):

    import os
    if os.path.exists(file_path):
        os.remove(file_path)

# remove_file_using_python("/Users/anilkumar/workspace/git_practice/all_topics/10interview_programs/sample.txt")


def check_given_number_is_prime(num2):
    for i in range(2, num2):
        if num2%i == 0:
            print(f"give number  {num2} is not prime number")
            break
    else:
        print(f"given number {num2} is prime number")

#
# check_given_number_is_prime(10)
# check_given_number_is_prime(5)


def generate_prime_numbers(start, end):
    out = []
    for i in range(start, end):
        for j in range(2,i):
            if i %j == 0:
                break
        else:
            out.append(i)
    print(out)


# generate_prime_numbers(10, 50)


def remove_duplicates_in_list(list3):
    # for i in list3:
    #     occ = list3.count(i)
    #     if occ > 1:
    #         for j in range(occ-1):
    #             list3.remove(i)
    # print(list3)

    for i in list3[:]:
        occ = list3.count(i)
        if occ > 1:
            list3.remove(i)
    print(list3)


# remove_duplicates_in_list([1,4,5,6,4,1,5])


def valid_ip_address1(ip_add):
    import re
    pattern = "^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))$"
    if re.search(pattern, ip_add):
        print(f"given ip add {ip_add} is valid")
    else:
        print(f"given ip add {ip_add} is invalid")


# valid_ip_address1("10.10.10.1000")
# valid_ip_address1("10.1.1.193")

def valid_ip_address2(ip_add):
    import re
    pattern = "^(\d{1,3}\.){3}\d{1,3}$"
    if not re.search(pattern, ip_add):
        print(f"given ip add {ip_add} is invalid")
        return False
    bytes = ip_add.split(".")
    for ip_byte in bytes:
        if int(ip_byte) < 0 or int(ip_byte) > 255:
            print(f"ip address {ip_add} is invalid because of {ip_byte}")
            return False
    print(f"given ip add {ip_add} is valid")
    return True

# print(valid_ip_address2("10.10.10.990"))
# print(valid_ip_address2("10.1.1.193"))

#09:9e:8f:5d:23:2a


def valid_mac_address(mac_address):
    import re
    if re.search("^[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac_address.lower()):
        print("mac address is valid")
    else:
        print("invalid")


# valid_mac_address(mac_address="00:29:15:80:4E:4A")

# def valid_email(email)
#     import re
#     if re.search("[A-Za-z]")

def fibonacci_series(num):
    a = 0
    b = 1
    print (a)
    for i in range(num):
        c = a + b
        print(c)
        b = a
        a = c

# fibonacci_series(10)


def rotate_given_array(list2, n):
    for i in range(n+1):
       list2.append(i)
       list2.remove(i)
    print(list2)

# rotate_given_array(list2=[1,2,3,4,5,6], n=4)