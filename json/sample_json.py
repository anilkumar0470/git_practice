import json

data = """{"employees":[  
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com", "loc":"Bang"},  
    {"name":"Bob", "email":"bob32@gmail.com", "loc":"Hyd"},  
    {"name":"Jai", "email":"jai87@gmail.com", "loc":"City"}  
]}  """

# # loads is used to load the json string into dict
# content = json.loads(data)
# print(type(content))
# for person in content["employees"]:
#     del person["email"]
#
# print(type(content))
# # dumps is used to convert python dict json string
# new_content = json.dumps(content, indent=2, sort_keys=True)
# print(type(new_content))
#
# print(new_content)

# with open("json_content_usa.json") as fd:
#     data = json.load(fd)
# for state in data["states"]:
#     del state["abbreviation"]
# with open("new_states.json", "w") as f :
#     json.dump(data, f, indent=4)

