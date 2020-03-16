a = 6
b = 5
print(a + b)
print(a-b)
print(a * b)
print(a/b)
print(a%b)
print(a//b)


s =  set()
input_list = ["Sam", "San"]
def sample(word):
    if word[0] == "S":
        return True
    else :
        pass
out = list(map(sample, input_list))
count =  0
for i in out :
    if i :
        count = count + 1
print(count)


print(((500//7)%5)**3)

s = "I love Python"
print(s[2:6])


def sample(num):
    fact = 1
    if num  ==  0 :
        return 1
    elif num > 1 :
        for i in range(1, num + 1):
            fact = fact * i
        return fact
print(sample(1))



# Read the three input lists, i.e. 'C', 'F', and 'H'.
import ast,sys
input_str = sys.stdin.read()
input_list = ast.literal_eval(input_str)
C = input_list[0]
F = input_list[1]
H = input_list[2]

# Convert the given lists to sets as it is easier to perform the given operations
# on sets
C = set(input_list[0])
F = set(input_list[1])
H = set(input_list[2])

# Perform an '&' operation between the three sets to find out the students who play
# all the three sports. Finally, convert it into a list, apply the sorted() function
# and print the resultant list.
print(sorted(list(C & F & H)))

# The following opeartion gives the students who play only Cricket and Football.
# Note that only (C & F) also contains the students who play all the three sports
# and hence, we need to subtract (C & F & H) from it.
print(sorted(list((C & F) - (C & F & H))))

# The students who play exactly three sports can be given by the following expression
# (C & F) gives the students who play cricket and football, (F & H) gives the students
# who play football and hockey, and (F & H) gives the students who play cricket and
# hockey. Performing an 'OR' operation ('|') between the three will give the students
# who play a minimum of two sports and finally subracting (C & F & H) will give the
# list of students who play exactly two sports.
print(sorted(list(((C & F) | (F & H) | (C & H)) - (C & F & H))))

# As the students are numbered from 1 to 20, the whole set of students can be defined
# by creating a set containing all the numbers from 1 to 20, using range. Finally,
# you can subract (C | F | H), from the created set to get all the students who don't
# play even a single sport.
print(sorted(list(set(range(1,21)) - (C | F | H))))


c = [2, 5, 9, 12, 13, 15, 16, 17, 18, 19]
f = [2, 4, 5, 6, 7, 9, 13, 16]
h = [1, 2, 5, 9, 10, 11, 12, 13, 15]

cc = set(c)
ff = set(f)
hh = set(h)
print(cc & ff & hh )
print(( cc & ff) - (cc & ff & hh))

# print(cc.intersection(ff,hh))
# print(ff.intersection(cc))