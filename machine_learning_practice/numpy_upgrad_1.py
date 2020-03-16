# numeric python module deals with scientific computing the data analysis
# here we need to write the vectorized code means , try to use parallelism as we are dealing big data .
# array is essentially is a list and which is homogeneous and which is n -dimensional.
import numpy as np
# Creating a 1-D array using a list
# np.array() takes in a list or a tuple as argument, and converts into an array
array_1d = np.array([2, 4, 5, 6, 7, 9])
print(array_1d)
print(type(array_1d))

# creating 2-dimensional array
array_2d = np.array([[1,2,3], [4,5,6]])
print(array_2d)
# to create n-d array we need to provide n-1 d array in side and inside n-2 d array and soon at the end it will come
# as single d array
# creating 3 d means in outer list we will provide 2d first later we will change to 1d
# axis = 0 refers to the rows
# axis = 1 refers to the columns
#
# Advantages of NumPy
# What is the use of arrays over lists, specifically for data analysis? Putting crudely, it is *convenience and speed *:
#
# You can write vectorised code on numpy arrays, not on lists, which is convenient to read and write, and concise.
# Numpy is much faster than the standard python ways to do computations.
# Vectorised code typically does not contain explicit looping and indexing etc. (all of this happens behind the scenes,
# in precompiled C-code), and thus it is much more concise.
#
# Let's see an example of convenience, we'll see one later for speed.
list_1 = [3, 6, 7, 5]
list_2 = [4, 5, 1, 7]
# using map
product_list =  list(map(lambda x,y : x * y , list_1, list_2))
print("prodcut list is {}".format(product_list))
# the binary operations like +,_,* ,/ are element wise operations in array which can not be normal python list
# see example here .
array_1 = np.array(list_1)
array_2 = np.array(list_2)

# multiplying both array_1 and array_2
print("multiplication is {}".format(array_1 * array_2))
# adding of array
print("Addition is {}".format(array_1 + array_2))

# one more example between traditional python and num py python
square_list = [i ** 2 for i in list_1]
print("square list is {}".format(square_list))

square_array = array_1 ** 2
print("array square is {}".format(square_array))
# one qucik thing we need to remember is while doing binary operations we need to make sure dimension of both
# array must be same

# Convert lists or tuples to arrays using np.array()
# Note that np.array(2, 5, 6, 7) will throw an error - you need to pass a list or a tuple
array_from_list = np.array([2, 5, 6, 7])
array_from_tuple = np.array((4, 5, 8, 9))

print(array_from_list)
print(array_from_tuple)

# let say if you want to create 1000 x 1000 d array ..manually is it possible ..yes it is possible but as a human
# we will make lot of mistakes and it is time taken process as well.
# to avoid this problem numpy providing few functions to create array based user provided dimensions.

# ----------------------------------------------------------------------------------------
# zeros function is used to create array with all elements as zero
# ----------------------------------------------------------------------------------------
# arguments :
# shape - mandatory-- shape of the array --ex --2 or (2,3)-to specify rows and columns we need to use tuple/list
# dtype - optional -- by default it will take float and we can change according to your requirement
# creating zeros array with single value
print(np.zeros(4))
# creating zeros array with tuple as shape and data type as int
print(np.zeros((3,3), dtype="int"))

# ----------------------------------------------------------------------------------------
# ones function is used to create array with all elements as one
# ----------------------------------------------------------------------------------------
# arguments :
# shape - mandatory-- shape of the array --ex --2 or (2,3)-to specify rows and columns we need to use tuple/list
# dtype - optional -- by default it will take float and we can change according to your requirement
# creating ones array with single value
print(np.ones(4))
# creating ones array with tuple as shape and data type as int
print("ones example is {}".format(np.ones((5,3), dtype="int")))

# random function is used to create the array in between 0 and 1 with the given size and all values are uniformed ..i.e
# the difference between these values are same.

print("random array example is {}".format(np.random.random(3)))
print("random array example is {}".format(np.random.random([3,4])))

# ----------------------------------------------------------------------------------------------------------
# arange function is simillar to  range in python which is used to generate the sequence based on the input ,
# ----------------------------------------------------------------------------------------------------------
# provided by the user , it will take four  arguments
# start index --optional -- from where you want start-- if not provided it will take from zero
# end index --mandatory and end value is always excluded -- from where to end --
# step index -- optional ..how much we need to provide while generating the sequence
# dtype -- optional ..if not provided it will take it from the other fields.
# returns ndarray object
# example with only stop index
print(np.arange(10))
# example with start and stop index
print(np.arange(1, 10))
# example with start , stop and step index
print(np.arange(1,10, 2))
# we can also provide floating points as well better to use linspace for the same .
print(np.arange(10.0))
# complex numbers with provding the dtype argument
print(np.arange(10, dtype="complex"))
# for floating
print(np.arange(10, dtype="float"))

#-------------------------------------------------------------------------
# linspace -it simillar to arange but the difference is in linspace we will have breakpoint or num argument which is
# used to #  specify how many values u want have with in the given range --
# linear space method which is used to created array with even spaced values
# arguments
# start -- optional argument -- where to start-- by default it will be included
# stop -- mandatory -- where to stop ..by default it will be included ,
# num -- optional --default value is 50, how many evenly spaced numbers  you want in the specified range -we can provide
# user defined values according to requirement
# endpoint -- optional --by default True which means the stop index will be included while generating the sequence..
# if you want to exclude we can make this flag as False.
# retstep -- optional -- to see how spacing done or difference between two elements
print(np.linspace(1, 100, 5))
# it will generate evenly spaced five numbers as we specified 5  as num from the range of 1, 100 and also stop index is
# included here
# to exclude the stop index or value or endpoint
print(np.linspace(1, 100, 5, endpoint=False)) # stop value will not be included in the generated array ..however it will
# five evenly spaced values in the given range by excluding stop index.
# to find the difference between two elements or which number is used to do spacing
print(np.linspace(1, 100, 5, retstep=True))
# with start and stop index and num will be 50 by default and stop value will be included.
print(np.linspace(1, 100))

# Creating a 4 x 3 array of 7s using np.full()
# The default data type here is int only
# arguments shape - size of the array
# value -- by which value we need to create it can be any integer
print("full() example is {}".format(np.full((4,3), 8)))
print("full() example is {}".format(np.full((4,3), 80)))

#----------------------
# tile function is used to create array with input array and size of the array .
# ie. user will provide array and size ..by using given array tile function will generate the array of given size
# Given an array, np.tile() creates a new array by repeating the given array for any number of times that you want
# The default data type her is int only
print("tile example is {}".format(np.tile([1,2,3], (3))))
print("tile example is {}".format(np.tile([4,5,6], (3,3))))

# eye function is used to create identity matrix
# arguments size -mand -size of array i. e only one value i.e if user provided 2 as value it will create 2 X 2 and so on
# dtype --optional --by default float we can change int as well
print("eye example is {}".format(np.eye(2)))
print("eye example is {}".format(np.eye(3, dtype="int")))

# Create a 4 x 4 random array of integers ranging from 0 to 9
print("example of random array with given values {}".format(np.random.randint(0, 10, (4,4))))

print(np.full((3,4), 6))

# when we are loading actual data or csv file the data will be more hence loading/fething the entire data is not
# good so we will use slicing or accessing few columns or rows
array = np.random.random([1000,300])
# accessing second row index always start from zero
print(array[1, ])
# to get the info of array
print("shape of array is {}".format(array.shape))
print("data type of array is {}".format(array.dtype))
print("dimensions of the array is {}".format(array.ndim))
print("memory occupied by array is {}".format(array.itemsize))

# create 3d array
# by default arange will generate 1d to change the dimensions we will reshape method and the mutliplication of
# values in re shape method must same as value in arnage function
array_3d = np.arange(24).reshape(2,3,4)
print(array_3d)
# if see the output we have two slices seperated by space in each we have 3 rows of 4 columns.

# Accessing , slicing and iteration
array_oned = np.arange(10)

# accessing third element
print(array_oned[2])

# accessing multiple elements we need to provide as list
print(array_oned[[2,5, 6]])

# accessing from fourth element onwords
print(array_oned[3:])

# accessing third to seventh element
print(array_oned[2:7])

# example with step
print(array_oned[0::2])

# iteration and index is similar to array and iterating on array is not good as we are dealing with large data.

#######################################
# Accessing multi dimensional array's #
#######################################
# accessing 2d arrays will differ from one d and we will similar to matrix like if you want to access 2nd row third
# element then we will specify like m(2,3) where m is matrix .. similarly we will access by providing both values
# in the list
#          axes 1
#       0       1          2
# a o   0,0     1,0        2,0
# x 1   1,0     1,1        1,2
# e 2   2,0     2,1        2,2
# s
# 0
# the above table will represent how to acess the elements from 2d
array_twod = np.array([[2,4,6,8], [1,3,5,7], [7,8,9,10]])
print(array_twod)
# two access third row second element
print(array_twod[2, 1])
# slicing will work as usual for 2d also
# it will 2 nd row with all elements as we didn't specified column
print(array_twod[2, :])
# it will display thrid column of all rows
print(array_twod[:, 3])
# slicing all rows with first two columns
print(array_twod[:, :2])
# slicing all rows with first three coulmns
print(array_twod[:, :3])

# Iterating over 2-D arrays
# and it will take n-1 d as single element i.e let say if you are iterating through the 3d array then for loop will
# print 2d array as single element and so on upto 1d array.
print("for loop example for 2d ")
for row in array_2d:
    print(row)

# Iterating over 3-D arrays: Done with respect to the first axis
array_3d = np.arange(24).reshape(2, 3, 4)
print(array_3d)

# problem in upgrad please use accessing the twod mechanism for the same specified in 208 line
test_array = np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])
print(test_array)
print("Accessing first column  {}".format(test_array[:,0]))
print(" Acessing the first row {}".format(test_array[0, :]))
print("Accessing the last column {}".format(test_array[:,3]))
print("Accessing the last row {}".format(test_array[2, :]))
print("Accessing first two rows {}".format(test_array[:2, :]))
print("Accessing first two coulmns  {}".format(test_array[:, :2]))

# computation time in numpy and normal python list
# one thumb rule is never use for in numpy as we are dealing with large data set which indirectly the data manipulation
# code is not upto the mark.
# always use numpy(Vectorized ) compared to normal python
# example for comparing the normal python vs numpy
# creating two lists
import time
list1 = [i for i in range(1000000)]
list2 = [j ** 2 for j in range(1000000)]
t0 = time.time()
result_list = list(map(lambda x,y : x * y, list1, list2 ))
t1 = time.time()
list_time = t1 - t0

array1 = np.array(list1)
array2 = np.array(list2)
t0 = time.time()
res_list = array1 * array2
t1 = time.time()
numpy_time = t1 - t0
print(t1-t0)
print("time taken for normal python {} and numpy {}".format(list_time, numpy_time))

