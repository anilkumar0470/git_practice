import re

#res=re.match((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[0]*[0-9][0-9]*)\.(25[0-5]|2[0-4][0-9]|[01][0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?),a)

import numpy as np
c = np.array([[5,6,7],[7,6,5],[0,8,7]])
print(c.shape)
print(c[:,1])

# Read the input list
import numpy as np

# Convert the input list to a NumPy array
array_2d =np.array([[11, 12, 13, 14], [21, 22, 23, 24], [31, 32, 33, 34]])

# Extract the number of rows and columns of the array
rows = len(array_2d[:, 0])
cols = len(array_2d[0, :])

# Extract the first column, first row, last column and last row respectively using
# appropriate indexing
col_1 = array_2d[:, 0]
row_1 = array_2d[0, :]
col_last = array_2d[:, cols-1]
row_last = array_2d[rows-1, :]

print(col_1)
print(row_1)
print(col_last)
print(row_last)


import numpy as np
seed=0
n=10
p=0.5
#write your code here
np.random.seed(0)
s = np.random.binomial(n, p, n)
print(s)

# import scipy.stats
# scipy.stats.norm(100, 12).pdf(98)


# Python 3.x code to demonstrate star pattern

# Function to demonstrate printing pattern of numbers
def numpat(n):
    # initialising starting number
    num = 1
    # outer loop to handle number of rows
    for i in range(0, n):
        # re assigning num
        num = 1
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i + 1):
            # printing number
            a  = "{}".format(num)
            print(int(a), end="")
            # incrementing number at each column
            num = num + 1
        for k in range(i ,0,-1):
            # printing number
            b = "{}".format(k)
            print(int(b), end="")
            # incrementing number at each column

        # ending line after each row

        if  i != n-1 :
            print("\r")

# Driver code
n = 4
# numpat(n)



# for i in range(1,5):
#     print (((10 ** i - 1) // 9) ** 2)
import math
print (0.5 * (1 + math.erf(100 - 90)/math.sqrt(2 * 10**2)))

# from statistics import NormalDist
#
# NormalDist(mu=100, sigma=12).pdf(98)
#
# n = 15
# a =  n - 3
# b = n - 1
# c  = a/b
# d = "{:.4f}".format(c)
# e = float(d)
# print(e)
j  = 100
if j > 10 and j < 200 :
    print("ss")
# import pandas as pd
# df  = pd.read_csv("sample.csv")
# df.sort_values("ff",ascending=True)

lisst = ["USA", "IND"]
import requests
from bs4 import BeautifulSoup

html_page  = requests.get("https://en.wikipedia.org/wiki/List_of_territorial_entities_where_English_is_an_official_language")
print(dir(html_page))
print(html_page.content)
soup = BeautifulSoup(html_page.content, 'html5lib')
print(soup)
print(soup.prettify())

# data_frame1 = ''
# data_frame1 =
#
# data_frame1.loc[dataframe_1["funding_round_type"] >= 5000000 and  [dataframe_1["funding_round_type"] < 150000000,["permalink", "funding_round_type", "raised_amount_usd", "category_list",  "country_code" ]]


import time

start_time = time.time()
def sample():
    for i in range(100000):
        print("aa")
sample()
end_time = time.time()
print(end_time-start_time)