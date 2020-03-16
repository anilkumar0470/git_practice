import pandas as pd
# read_csv method is used to read the csv file and it will return the entire data as object
# to see/fetch the data
df = pd.read_csv("C:\\Users\\Terralogic\\Desktop\\hello.csv")
print(df)
# to display the rows and columns in tuple
print(df.shape)
# head  to print some starting data in the table
print(df.head())
# to print upto particular row numbers from the starting
print(df.head(2))
# tail to display the ending data
print(df.tail())
# to print upto particular row numbers from the ending
print(df.tail(2))
# to access multple rows in between
print(df[2:5])
# to access particular coulmn
print(df["day"]) # df.day also will work as df is dictionary
# to access only few columns from the table
print(df[["day","event","temperature"]])

print("======================")
# to edit the data or process the data
# to find max number in the column
print(df.temperature.max())
# to find min number in the column
print(df.temperature.min())
# to find the mean of the column
print(df["temperature"].mean())
# to find the standard deviation of the column
print(df["temperature"].std())
# describe method will do analysis on the table it will show some information about all integer columns which is useful
# like length, mean, min_number, max_number, 25%, 50% and 75%...
#        temperature  windspeed
# count     6.000000   6.000000
# mean     30.333333   4.666667
# std       3.829708   2.338090
# min      24.000000   2.000000
# 25%      28.750000   2.500000
# 50%      31.500000   5.000000
# 75%      32.000000   6.750000
# max      35.000000   7.000000
print(df.describe())

# if you want ot apply any filter(like to get the > all values or < all values ) then it is simillar to sql
print(df[df["temperature"]>=32])
# to find the maximum temperature row
print(df[df.temperature == df["temperature"].max()])
# to find the minimum temperature row
print(df[df["temperature"]==df["temperature"].min()])
# to find the max temp row with few columns only
print(df["day"][df["temperature"]==df.temperature.max()])
# Tip some times column name might contain spaces so better to use df["temperature"] like this.
# By default pandas will allocate the numbers from zero length of rows -1
print(df.index)
# set_index() is used to set index as any column .. and return the result as output and we can store that output one
# variable and we can use further where as if you want to apply the changes in the current data frame use inplace=True
# if you want to change the index to any column use below syntax and inplace=True it will modify the current data
# frame
df.set_index('day', inplace=True)
# once you set the index we can fetch any row based coulmn value
print(df.loc["1/4/2017"])
# to change the index from user defined column name to pandas predefined one
df.reset_index(inplace=True)
df.set_index("event", inplace=True)
# if multiple occurances available with the same column index , it will return both
print(df.loc["Snow"])
df.reset_index(inplace=True)
print(df)



# =====================================================================
# =====================================================================



