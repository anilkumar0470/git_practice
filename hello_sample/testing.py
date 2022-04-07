import json

fd = open("sample.json")

json_content = json.load(fd)

print(json_content)

for element in json_content["employess"]:

    for key,value in element.items():
        if type(value["age"]) == int:
            print("age is int for {} ".format(key))
        else:
            print("the age for this is not int {}".format(key))


