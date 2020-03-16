# pandas is built by using the numpy for data analysis.
# in pandas we will have two important things . data frame and series
# in numpy we will do operations on each element where as in the series we will do iterations and series will hold may
# not data it will hold meta data index .
# series : similar to 1-d array containing scalar values of same type
# data frame: 2d array  is a simply table where each column is a series.
# columns will have column names which are nothing but attributes
# rows will have indexes
import pandas as pd

################################
# Series is method is used to create a series it is similar to create a array .
# by default index will be assigned to the each element in the series and index is always start from zero.
sample_series = pd.Series((1,2,3,4,5))
print(sample_series)
print(type(sample_series))
one_series = pd.Series(["a", "b", "af"])
print(one_series)

# creating a series of type datetime
date_series = pd.date_range(start = '11-09-2017', end = '12-12-2017')
#print(date_series)
type(date_series)

# Indexing pandas series: Same as indexing 1-d numpy arrays or lists
# accessing the fourth element
print(sample_series[3])

# accessing elements starting index = 2 till the end
print(sample_series[2:])

# accessing the second and the fourth elements
# note that s[1, 3] will not work, you need to pass the indices [1, 3] as a list inside the original []
print(sample_series[[1, 3]])

# apply is method used apply the user defined method on series
print(sample_series.apply(lambda x:x **2 ))

# Assuming that each value in the column must be same data type
# creating data frame using dictionary
data_frame = pd.DataFrame({'name': ['Vinay', 'Kushal', 'Aman', 'Saif'],
                   'age': [22, 25, 24, 28],
                    'occupation': ['engineer', 'doctor', 'data analyst', 'teacher']})
# print(data_frame)
# generally we will use csv file to create data frame as it is the data and we can not  create the data frame manually
# with the given data like above.
##############################
# read_csv method is used to read the csv file
#############################
market_df = pd.read_csv("market_fact.csv")
print(market_df)

# to display the rows and columns in tuple
print(market_df.shape)
# head  to print first five rows data in the table
print(market_df.head())
# # to print upto particular row numbers from the starting, it will display the n number of rows from the starting
print(market_df.head(2))
# # tail to display the ending data
print(market_df.tail())
# # to print upto particular row numbers from the ending
print(market_df.tail(2))
# # to access multiple rows in between
print(market_df[2:6])
################################################
# info() method used to display the information about data frame
# like number of columns and name of the coulmns and no of entries in entries in data frame , num of entries in each
# column there may be chance of some of the values are null.
# .<class 'pandas.core.frame.DataFrame'>
# RangeIndex: 8399 entries, 0 to 8398
# Data columns (total 10 columns):
# Ord_id                 8399 non-null object
# Prod_id                8399 non-null object
# Ship_id                8399 non-null object
# Cust_id                8399 non-null object
# Sales                  8399 non-null float64
# Discount               8399 non-null float64
# Order_Quantity         8399 non-null int64
# Profit                 8399 non-null float64
# Shipping_Cost          8399 non-null float64
# Product_Base_Margin    8336 non-null float64
# dtypes: float64(5), int64(1), object(4)
# memory usage: 656.3+ KB
market_df.info()

#####################################
# #describe method will do analysis on the table it will show some information about all integer columns which is useful
# # # like length, mean, min_number, max_number, 25%, 50% and 75%...
# Sales     Discount  ...  Shipping_Cost  Product_Base_Margin
# count   8399.000000  8399.000000  ...    8399.000000          8336.000000
# mean    1775.878179     0.049671  ...      12.838557             0.512513
# std     3585.050525     0.031823  ...      17.264052             0.135589
# min        2.240000     0.000000  ...       0.490000             0.350000
# 25%      143.195000     0.020000  ...       3.300000             0.380000
# 50%      449.420000     0.050000  ...       6.070000             0.520000
# 75%     1709.320000     0.080000  ...      13.990000             0.590000
# max    89061.050000     0.250000  ...     164.730000             0.850000
print(market_df.describe())

##########################
# columns method to display the columns
print(market_df.columns)

# values will method all values keep it in array
print(market_df.values)

# for every row in data frame will have index and index is always start from zero
# we can change the index, we can set the index as column it self.
# set_index () to set the index it will column name as argument
market_df.set_index("Ord_id", inplace=True)
print(market_df.head())
# after applying our index we can sort by index level.. even before applying setindex also we can do sorting ..however
# those are already in ascending order.
print(market_df.sort_index(ascending=False))

# we can also sort at column level and we need to provide column name as value for sort values
print(market_df.sort_values(by="Sales").head())

# Sorting in decreasing order of Shipping_Cost
market_df.sort_values(by='Shipping_Cost', ascending = False).head()

# Sorting by more than two columns
# Sorting in ascending order of Sales for each Product
market_df.sort_values(by=['Prod_id', 'Sales'], ascending = False)

# # to access particular column
# print(df["day"]) # df.day also will work as df is dictionary
# # to access only few columns from the table
# print(df[["day","event","temperature"]])
#
# print("======================")
# # to edit the data or process the data
# # to find max number in the column
# print(df.temperature.max())
# # to find min number in the column
# print(df.temperature.min())
# # to find the mean of the column
# print(df["temperature"].mean())
# # to find the standard deviation of the column
# print(df["temperature"].std())
# # describe method will do analysis on the table it will show some information about all integer columns which is useful
# # like length, mean, min_number, max_number, 25%, 50% and 75%...
# #        temperature  windspeed
# # count     6.000000   6.000000
# # mean     30.333333   4.666667
# # std       3.829708   2.338090
# # min      24.000000   2.000000
# # 25%      28.750000   2.500000
# # 50%      31.500000   5.000000
# # 75%      32.000000   6.750000
# # max      35.000000   7.000000
# print(df.describe())
#
# # if you want ot apply any filter(like to get the > all values or < all values ) then it is simillar to sql
# print(df[df["temperature"]>=32])
# # to find the maximum temperature row
# print(df[df.temperature == df["temperature"].max()])
# # to find the minimum temperature row
# print(df[df["temperature"]==df["temperature"].min()])
# # to find the max temp row with few columns only
# print(df["day"][df["temperature"]==df.temperature.max()])
# # Tip some times column name might contain spaces so better to use df["temperature"] like this.
# # By default pandas will allocate the numbers from zero length of rows -1
# print(df.index)
# # set_index() is used to set index as any column .. and return the result as output and we can store that output one
# # variable and we can use further where as if you want to apply the changes in the current data frame use inplace=True
# # if you want to change the index to any column use below syntax and inplace=True it will modify the current data
# # frame
# df.set_index('day', inplace=True)
# # once you set the index we can fetch any row based coulmn value
# print(df.loc["1/4/2017"])
# # to change the index from user defined column name to pandas predefined one
# df.reset_index(inplace=True)
# df.set_index("event", inplace=True)
# # if multiple occurances available with the same column index , it will return both
# print(df.loc["Snow"])
# df.reset_index(inplace=True)
# print(df)