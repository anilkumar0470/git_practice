import numpy as np
# -----------------------------------------------------
# array method is used to create array . we can provide list or tuple
# -----------------------------------------------------
# to create one dimensional array
sample_array = np.array([1,2,3])
print(sample_array)
# to create multi dimensional array we need to use ndim flag by default it is zero and  you need to specify the
# list or tuple as nested list so that it will treat as multi dimensional array at this time ndim flag is not needed as
# we are mentioning in nested list
two_dim_array = np.array([[1,2,3], [4,5,6]])
print(two_dim_array)
# ----------------------------------------------------------------------------------------------------------
# arange function is simillar to  range in python which is used to generate the sequence based on the input ,
# ----------------------------------------------------------------------------------------------------------
# provided by the user , it will take four  arguments
# start index --optional -- from where you want start-- if not provided it will take from zero
# end index --mandatory and end value is always excluded -- from where to end --
# step index -- optional ..how much we need to provide while generating the sequence
# dtype -- optionlal ..if not provided it will take it from the other fields.
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
print(np.ones((3,3), dtype="int"))

# ----------------------------------------------------------------------------------------
# empty function is used to create array with dummy values without initializing the values
# ----------------------------------------------------------------------------------------
# arguments :
# shape - mandatory-- shape of the array --ex --2 or (2,3)-to specify rows and columns we need to use tuple/list
# dtype - optional -- by default it will take float and we can change according to your requirement
# creating dummy values  array
print(np.empty(4))
# creating empty array with tuple as shape and data type as int
print(np.empty((3,3), dtype="int"))
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
print(np.linspace(1, 100,))