import json

string = """
{"employees":[
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}
"""

# converting json to dict
p_data = json.loads(string)
print(type(p_data))
print(p_data)
#
# for employee in p_data["employees"]:
#     print(employee["name"])
#     del employee["email"]
#
# converting python dict to json
new_string = json.dumps(p_data, indent=2)
print(new_string)
print(type(new_string))

# with open('sample.json') as f:
#     data = json.load(f)
# 
# for state in data['states']:
#     print(state['name'])
#     del state['area_codes']
# 
# with open('new_states.json', 'w') as fd:
#     json.dump(data, fd, indent=2)


# import pandas as pd

