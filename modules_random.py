#inbuilt modules are random,math,time,calendar,os,sys
# this is for choice
#choice is amethod in random and it will generate number randomly from the input
#"from random import choice" is used to select only one method
#method ---range---output
#random --- 0<r<1 --float
#randint---min<r<max ---int
#uniform --min<r<max--floating
import random
l = [23,34,45,56,67]
t = (10,23,20,25)
st = "a string"
print "  list  "
for i in range(5):
    print "choice is :",random.choice(l)
print " tuple "
for i in range(5):
    print "choce is :",random.choice(t)
print " string "
for i in range(5):
    print "choice is :",random.choice(st)
#random is a method is in random module and it will always generate number between zero and one
print "example of random"
for i in range(6):
    p = random.random()
    print "random number ",p
#shuffle is method in random and it will produce the output by shuffling the input
l = [11,22,33,44,55]
print "before shuffle",l
random.shuffle(l)
print "after shuffle",l

print random.randrange(10,100,2)
# output should be multiple of 2 may be
print random.randrange(10,100,3)
#output should be multiple of 3
print random.randrange(10,100,10)
#output should be multiple of 10
print random.randrange(10,20)
#output should be in the range of 10 to 20
print random.randrange(10)
#output is 1 to 10

#ranint is method to generate a random number between given range
print random.randint(10,20)
#randuniform is used to generate floating number between given range
print random.uniform(30,50)
print "example for range uniform"
for i in range(4):
    print "==>",random.uniform(30,50)