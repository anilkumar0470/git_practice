# a = int(input("enter a value"))
# b = int(input("enter b value "))
# if a == b :
#     c = 2 * (a+b)
#     print (c)
# else:
#     c = a + b
#     print(c)

# # to check leap year or not
# year = int(input("enter year to check like 2020:"))
# if year%4 == 0 :
#     print("leap year")
# else :
#     print("non leap year")

# to check given character is lower case or upper case
# string =  input("enter a char or string to check lower or upper case :")
# if string.islower():
#     print("given string is lower case")
# elif string.isupper():
#     print("given string is upper case")
# else:
#     print("it is combination of both or special characters included in the given string")
#
# # to check given string is alpha or not
# input_string = input("enter a char or string to check alphabet or not ")
# if input_string.isalpha():
#     print("given string is alphabet")
# else:
#     print("given string is not aplhabet")

# # to check uppercase or lower case alphabet
# input_string = input("enter a char to check lower or upper case alphabet")
# if input_string.isalpha():
#     if input_string.islower():
#         print("Given char lower case alphabet")
#     elif input_string.isupper():
#         print("Given char is upper case alphabet")
#     else :
#         print("given string is alphabet but combination of both lower and upper")
#

n = int(input("enter a number "))
if n  == 21 :
    print(0)
elif n > 21 :
    print(n - 21)
else :
    print(21 - n)