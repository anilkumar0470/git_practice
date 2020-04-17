#List is a datatype and it is an order collection of elements which is ant datatype
#including int,float,char,string,list,tuple,dictionary and object also

list = [1,2,3,"Good","Morning","welcome","to",'terralogic']
new_list = ["hai","hello","everyone"]

#Built in methods:
print len(list)
##it is used to display the length of the given list

print list.pop()
#This method is used to remove the last element in the list

print list.pop(5)
#This method is used to remove the element in the given index

print list.remove("anil")
#This method is used to remove the specified element directly and one time only

list.sort()
print list
#It used to arrange the list in the ascending order



list.reverse()
print list
#It is used to reverse the list


print list.index("welcome")
#It is used to display the index of given element(string or number)

list.append(new_list)
print list
list.append([10,100])
print list
#this is method is used to add the list into ending of another list and it will consider
#entire list as a single element and add it in the end of the list
#we can pass the name of the list as a parameter or elements


list.extend(new_list)
print list
list.extend([123,456])
print list


l = ['a','A',34,45,54,44,75,65,[34,56,44]]
for i in range(len(l)):
    print i ,"==",l[i]
