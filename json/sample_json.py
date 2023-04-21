import json
import os.path

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

# with open("questions_papers.json") as qfd:
#     new_data = json.load(qfd)
#     for question in new_data["questions"]:
#         print(question)
#         for key, value in new_data["questions"][question].items():
#             print(key, value)

import json
# function to add to JSON


def write_json(new_data, filename='new_states.json'):

    if not os.path.exists(os.path.join(os.getcwd(), "new_states.json")):
        with open(os.path.join(os.getcwd(), "new_states.json"), 'w') as f:
            data = {"tests": []}
            json.dump(data, f, indent=2)

    with open(filename, 'r+') as file:

        file_data = json.load(file)
        file_data["tests"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent=4)


y = {"name": "india12"}

write_json(y)
