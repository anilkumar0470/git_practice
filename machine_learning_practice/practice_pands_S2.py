# import pandas as pd
# # In some scenario's the column names   will start from other than first line .
# # To specify where columns are starting we need use skiprows arguments to skip the junk rows.
# # or even header argument also will do the same thing.
# df = pd.read_csv("C:\\Users\\Terralogic\\Desktop\\stock_data.csv", skiprows=1)
# df = pd.read_csv("C:\\Users\\Terralogic\\Desktop\\stock_data.csv", header=1)
# # if column names are not available in the given file, then we need to use header flag as None which means we are
# # telling that there is no headers for this data , apply according to your choice and by default pandas will
# # assign 0,1,2,3 ...how ever we can provide the names to columns/headers by using headers in csv_read method.
# df = pd.read_csv("C:\\Users\\Terralogic\\Desktop\\stock_data.csv", header=None, names=("col1","col2","col3","col4",
#                                                                                        "col5"))
# # read_csv method read the entire file/data if you want to read mulitple lines we can use nrows argument which is used
# # limit the rows .When we have million rows , this argument will be useful to set the limit of rows.
# # if we set nrows= 3 it will display 3 rows excluding column names row.
# df = pd.read_csv("C:\\Users\\Terralogic\\Desktop\\stock_data.csv", nrows=3)
# print(df)
# # NAN : not available numbers ..In every data some of the fields will be empty or filled with None or NA depending
# # on the data provides .In this case we need to replace all this none/NA values pandas understandable word , so that
# # why analyzing the data we will accurate values .
# # na_values=["not available", "n.a."] flag is used to specify all the junk strings , so that when python encounter the
# # strings specified in na_values it will keep NaN  in the all fields.
# df = pd.read_csv("C:\\Users\\Terralogic\\Desktop\\stock_data.csv", na_values=["not available", "n.a."])
# print(df)
# # when we ne_values as list it will apply to the entire table .so there may be scenario's like in some columns those
# # values must be needed , however we are keeping NAN as we are specifying as list. To avoid this we need specify the
# # ne_values as dictionary for each and every column. ne_values will be powerful to clean the data or data munzing or
# # data wrangling.
#
# df = pd.read_csv("C:\\Users\\Terralogic\\Desktop\\stock_data.csv", na_values={"eps": ["not available", "n.a."],
#                                                                               "revenue":["not available", "n.a.",-1],
#                                                                               "price":["not available", "n.a."],
#                                                                               "people":["not available", "n.a."]})
# print(df)
# # to_csv method is used to write content into csv file, by default it will add index also.To remove the index , we can
# # specify the index falg as False so that it will not write in to new csv file
# # to remove headers from csv file while writing use header flag as False
# df.to_csv("C:\\Users\\Terralogic\\Desktop\\write_data.csv", index=False, header=False)
# # if you want only specified columns to write into csv file use columns flag and index will removed by default as we
# # are using columns
# df.to_csv("C:\\Users\\Terralogic\\Desktop\\write_data1.csv", columns=["tickers", "eps"])


import pandas as pd
df = pd.read_csv("C:\\Users\\Terralogic\\Desktop\\missing_data.csv", parse_dates=["day"])
df.set_index("day", inplace=True)
# to fill all the nan values with 0 ..some times which is not good because some fields will expect strings if
# you take example name field we cannot keep 0 here .. to avoid this we can specify at each and every column
#new_df = df.fillna(0)
new_df = df.fillna({"temperature":0,
                    "windspeed":0,
                    "event":"no event"})
print(new_df)