# #Tuple(*) as argument
#
# def totalmarks(name,m1,m2,m3):
#     total = m1 + m2 + m3
#     print ("name is :",name)
#     print ("total marks: ",total)
#
# # totalmarks("anil",78,77,70)
#
#
# def something(name, *marks):
#     print ("name is : ",name)
#     print(type(marks))
#     total = 0
#     for i in marks:
#         total = total + i
#     print( "total:",total)
# something("anil",70,45,65,45,9, 454, 5454,6767)





l =  ["kesav", "shilpa"]
t = (l)

l.append("good")
print(t)



import json

it is string
d = """{
    "employees":{"name1": "test1",
                 "name2": "test2",
                 "name3": "test2"
                 },
    "salary":{
        "name1": 1000,
        "name2":10000,
        "name3": 3000

    }

}"""
dict_new = json.loads(d)
print(type(dict_new))

#the output is dict we can do dict methods here
for key, in dict_new.keys():
    print(key)