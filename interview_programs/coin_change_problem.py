n = 10
s = {2, 3, 5, 6}
list1 = []
#
# total  = 0
# for i in s :
#     for j in range(n):
#         total = total + i
#         if total == n:
#             pass
#
def count(S, m, n):
    # table[i] will be storing the number of solutions for
    # value i. We need n+1 rows as the table is constructed
    # in bottom up manner using the base case (n = 0)
    # Initialize all table values as 0
    table = [0 for k in range(n + 1)]
    print(table)

    # Base case (If given value is 0)
    table[0] = 1

    # Pick all coins one by one and update the table[] values
    # after the index greater than or equal to the value of the
    # picked coin
    for i in range(0, m):
        for j in range(S[i], n + 1):
            table[j] += table[j - S[i]]

    return table[n]


# # Driver program to test above function
# arr = [1, 2, 3]
# m = len(arr)
# n = 4
# x = count(arr, m, n)
# print(x)

# import sys
#
#
# # m is size of coins array (number of different coins)
# def minCoins(coins, m, V):
#     # base case
#     if (V == 0):
#         return 0
#
#     # Initialize result
#     res = sys.maxsize
#
#     # Try every coin that has smaller value than V
#     for i in range(0, m):
#         if (coins[i] <= V):
#             sub_res = minCoins(coins, m, V - coins[i])
#
#             # Check for INT_MAX to avoid overflow and see if
#             # result can minimized
#             if (sub_res != sys.maxsize and sub_res + 1 < res):
#                 res = sub_res + 1
#
#     return res
#
#
# # Driver program to test above function
# coins = [9, 6, 5, 1]
# m = len(coins)
# V = 11
# print("Minimum coins required is", minCoins(coins, m, V))
#
# # This code is contributed by
# # Smitha Dinesh Semwal


def findMin(V):
    # All denominations of Indian Currency
    deno = sorted([50,10,20,33,5,2,1])
    n = len(deno)

    # Initialize Result
    ans = []

    # Traverse through all denomination
    i = n - 1
    while (i >= 0):

        # Find denominations
        while (V >= deno[i]):
            V -= deno[i]
            ans.append(deno[i])

        i -= 1

    # Print result
    for i in range(len(ans)):
        print(ans[i], end=" ")


# Driver Code
if __name__ == '__main__':
    n = 55
    print("Following is minimal number",
          "of change for", n, ": ", end="")
    findMin(n)

# This code is contributed by
# Surendra_Gangwar






print()

import copy

l1 = [1,2,3,[4,5,6]]
l2 = l1
l2[3][0] = 9
print("l1", id(l1))
print("l2", id(l2))

print(l1)
print(l2)

# class Sam():
#     def __init__(self):
#         print(self)
#
# s = Sam()
# print(s)


str = "good evening"
a = 5
b = 10
def sample_decorator(original_fun):
    def wrapper_func(a,b, string ):
        return_value = original_fun(a,b,string)
        return return_value
    return wrapper_func
@sample_decorator
def sum(a,b, string):
    return a + b, string

a,b = 1, 2
string = "good evning"
print(sum(a,b, string))


for i in range(4):
    for j in range(3):
        print("0", end=" ")
    print()

a = int
b = input
print(a,b)