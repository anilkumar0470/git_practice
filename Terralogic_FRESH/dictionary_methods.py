d = {"name":"anil",'age':23,'loc':'koromangala'}

print d.keys()
#To display all the keys
print d.values()
#To display all the values
print d.items()
#To display all items(both keys and values)

print d.has_key('age')
#It is used to check whether
print d.clear()
#It is used to clear the dictionary
d1 = d.copy()
#to copy the dictionary
print d1
print d.pop("loc")
#to remove key and value
print d.popitem()
#it will randomly remove one key and value