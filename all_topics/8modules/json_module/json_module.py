import json

# loads -- used to string to dict
# dumps -- used convert json to string
# load  -- load json file content to dict
# dump  -- store content into json file


# # loads -- used to string to dict
#
# string = """{"candidates":
#               [
#                   {
#                       "name": "anil",
#                       "loc": "bangalore",
#                       "mob": "888"
#                   },
#                   {
#                       "name": "Kumar",
#                       "loc": "pune",
#                       "mob": "123"
#                   }
#               ]
# }"""
#
# new_dict = json.loads(string)
# print(new_dict)
# print(type(new_dict))
#
#
# # dumps -- used convert json to string
# json_dict = {"candidates":
#               [
#                   {
#                       "name": "anil",
#                       "loc": "bangalore",
#                       "mob": "888"
#                   },
#                   {
#                       "name": "Kumar",
#                       "loc": "pune",
#                       "mob": "123"
#                   }
#               ]
# }


# string_obj = json.dumps(json_dict)
# print(string_obj)
# print(type(string_obj))

# load -- load json file content to dict

fd = open("questions_papers.json", "r")
json_content = json.load(fd)
print(json_content)
print(type(json_content))










# # dump -- store content into json file
#
fd2 = open("test_new.json", "w")
json.dump(json_content, fd2, indent=5)
