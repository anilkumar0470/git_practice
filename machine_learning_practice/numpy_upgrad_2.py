# basic operations on array
# we can manipulate the arrays i.e we can change the shape , combining and splitting etc.
# here we will do vectorized operations
import numpy as np
# reshape () method used to reshape the array
# reshaping one d array to two d array
some_array = np.arange(12).reshape(3,4)
print(some_array)
# we can reshape again ..when we reshaping make sure that the prodcut of column and row value must be equal to the
# product of row and column value i.e 2*6 = 3 *4
print(some_array.reshape(2, 6 ))
# if we specifiy any one of the dimension for reshape as -1 then reshape method automatically the second one.
print(some_array.reshape(4, -1))
# to change the columns as rows and rows as coulmns we will use transpose
print(some_array)
print(some_array.T)

# vertical stacking .. adding one array to another array i.e up and down side -- no of coulmns must be same
list_1 = np.arange(15).reshape(3,5)
list_2 = np.arange(20).reshape(4,5)

array_1 = np.array(list_1)
array_2 = np.array(list_2)
print(array_1)
print("\n")
print(array_2)
# vertical stacking
print(np.vstack([array_1, array_2]))

# horizantal stacking .. adding one array to another array i.e side by side --no of rows must be same
list1 = np.arange(15).reshape(3,5)
list2 = np.arange(12).reshape(3,4)

array1 = np.array(list1)
array2 = np.array(list2)
print(array1)
print("\n")
print(array2)
# horizantal  stacking
print(np.hstack([array1, array2]))

# performing mathmatical operations on arrays are easy and each of these opertions are vectorized in numpy..vectorized
# means it will apply the selected operation on all elements in the given array
# Basic mathematical operations
a = np.arange(1, 20)

# sin, cos, exp, log
print(np.sin(a))
print(np.cos(a))
print(np.exp(a))
print(np.log(a))

# we can also create user defined functions to do operations on array but we need to make sure that we are telling to
# numpy this function is vectorized manner.then we can apply as simillar to other methods.
# non numpy way is not recommended.
a_list = [x/(x+1) for x in a]
print(a_list)
# instead of creating non numpy .. use vectorize method to create own functions
f = np.vectorize(lambda x : x/x+1)
print(f(a))

# basic linear algebra operations means linalg
# NumPy provides the np.linalg package to apply common linear algebra operations, such as:
# inv() is used to inverse the matrix
# det() is used to determinant the matrix
# eig() eigen values and  eigen vectors
# dot() is used to multiply two arrays.