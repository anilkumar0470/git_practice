# fd = open("sample.txt", "w")
# fd.seek(0,5)
#
# for i in range(1,11):
#     fd.write("2 * {}  = {}\n".format(i, 2 * i))
# fd.close()
# with open("sample.txt", "w") as fd :
#      for i in range(1,11):
#          fd.write("2 * {}  = {}\n".format(i, 2 * i))
# fd = open("sample.txt", "r")
# count = 0
# for line in fd.readlines():
#     value = line.count("the")
#     count = count + value
# print(count)
# fd.close()

fd = open("pokemon.csv", "r")
d = {}
for line in fd.readlines():
    list = line.split(",")
    key = list[0]
    value = list[1].strip()
    if value not in d:
        d.update({value : [key]})
    elif value in d:
        d[value].append(key)
print(d)
for k,v in d.items():
     print("key {}, no of times : {}".format(k, len(v)))
