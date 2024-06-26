

def bye():
    print("bye bye")

l1 = [10,2,10,3,4,2,10,34,2]


for element in l1:
    occ = l1.count(element)
    if occ >1 :
        for jj in range(occ-1):
            l1.remove(element)

print(l1)

