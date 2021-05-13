# Given a String of length S, reverse the whole string without reversing the individual words in it. Words are separated by dots.
#
# Input:
# The first line contains T denoting the number of testcases. T testcases follow. Each case contains a string S containing characters.
#
# Output:
# For each test case, in a new line, output a single line containing the reversed String.
#
# Constraints:
# 1 <= T <= 100
# 1 <= |S| <= 2000
#
# Example:
# Input:
# 2
# i.like.this.program.very.much
# pqr.mno
#
# Output:
# much.very.program.this.like.i
# mno.pqr

user_input = "i.like.this.program.very.much"
words = user_input.split(".")
words = reversed(words)
print(".".join(words))

# Given
# a
# string
# S.The
# task is to
# print
# all
# permutations
# of
# a
# given
# string.
#
# Input:
# The
# first
# line
# of
# input
# contains
# an
# integer
# T, denoting
# the
# number
# of
# test
# cases.Each
# test
# case
# contains
# a
# single
# string
# S in capital
# letter.
#
# Output:
# For
# each
# test
# case, print
# all
# permutations
# of
# a
# given
# string
# S
# with single space and all permutations should be in lexicographically increasing order.
#
# Constraints:
# 1 ≤ T ≤ 10
# 1 ≤ size
# of
# string ≤ 5
#
# Example:
# Input:
# 2
# ABC
# ABSG
#
# Output:
# ABC
# ACB
# BAC
# BCA
# CAB
# CBA
# ABGS
# ABSG
# AGBS
# AGSB
# ASBG
# ASGB
# BAGS
# BASG
# BGAS
# BGSA
# BSAG
# BSGA
# GABS
# GASB
# GBAS
# GBSA
# GSAB
# GSBA
# SABG
# SAGB
# SBAG
# SBGA
# SGAB
# SGBA
#
# Explanation:
# Testcase
# 1: Given
# string
# ABC
# has
# permutations in 6
# forms as ABC, ACB, BAC, BCA, CAB and CBA.
#
# ** For
# More
# Input / Output
# Examples
# Use
# 'Expected Output'
# option **

from itertools import permutations

comb = permutations("ABC")
print(comb)
l = ["".join(i) for i in comb]
print(l)

combinations = permutations("ABSG")
print(combinations)
ll = ["".join(i) for i in combinations]
print(ll)

#
# Given a string S, find the longest palindromic substring in S. Substring of string S: S[ i . . . . j ] where 0 ≤ i ≤ j < len(S). Palindrome string: A string which reads the same backwards. More formally, S is palindrome if reverse(S) = S. Incase of conflict, return the substring which occurs first ( with the least starting index ).
#
# NOTE: Required Time Complexity O(n2).
#
# Input:
# The first line of input consists number of the testcases. The following T lines consist of a string each.
#
# Output:
# In each separate line print the longest palindrome of the string given in the respective test case.
#
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ Str Length ≤ 104
#
# Example:
# Input:
# 1
# aaaabbaa
#
# Output:
# aabbaa
#
# Explanation:
# Testcase 1: The longest palindrome string present in the given string is "aabbaa".
test_input = "aaaabbaaccddcc"
d  = {}
for i in range(len(test_input)):
    for j in range(i, len(test_input)+1):
        sampel_str = test_input[i:j]
        reverse_str = sampel_str[::-1]
        if sampel_str == reverse_str and sampel_str:
            d.update({sampel_str:len(sampel_str)})
max_value = max(d.values())
for k,v in d.items():
    if v == max_value:
        print(k,v)

# de  = {k for k,v in d.items() if v == max_value}
# print(de)
#
# Given
# a
# string
# s, recursively
# remove
# adjacent
# duplicate
# characters
# from the string
#
# s.The
# output
# string
# should
# not have
# any
# adjacent
# duplicates.
#
# Input:
# The
# first
# line
# of
# input
# contains
# an
# integer
# T, denoting
# the
# no
# of
# test
# cases.Then
# T
# test
# cases
# follow.Each
# test
# case
# contains
# a
# string
# str.
#
# Output:
# For
# each
# test
# case, print
# a
# new
# line
# containing
# the
# resulting
# string.
#
# Constraints:
# 1 <= T <= 100
# 1 <= Length
# of
# string <= 50
#
# Example:
# Input:
# 2
# geeksforgeek
# acaaabbbacdddd
#
# Output:
# gksforgk
# acac
#
# ** For
# More
# Input / Output
# Examples
# Use
# 'Expected Output'
# option **

sample_input = "acaaabbbacdddd"
string = ""
l = []
for u in range(len(sample_input)):
    # print(u)
    #for v in range(u + 1 ,len(sample_input)):
    if len(sample_input) > u + 1:
        print(sample_input[u], sample_input[u + 1])
        if sample_input[u] == sample_input[u + 1]:
            #print(sample_input[u], sample_input[v])
            l.append(u)
            l.append(u + 1)
            print("aa")
print(l)
st = ""
for o in range(len(sample_input)):
    if o not in l :
      st = st + sample_input[o]

print(st)
#
# Given a string, the task is to remove duplicates from it. Expected time complexity O(n) where n is length of input string and extra space O(1) under the assumption that there are total 256 possible characters in a string.
#
# Note: that original order of characters must be kept same.
#
# Input:
# First line of the input is the number of test cases T. And first line of test case contains a string.
#
# Output:
# Modified string without duplicates and same order of characters.
#
# Constraints:
# 1 <= T <= 15
# 1 <= |string|<= 1000
#
# Example:
# Input:
# 2
# geeksforgeeks
# geeks for geeks
#
# Output:
# geksfor
# geks for

l = []
input_from_user = "geeks for geeks"
for i in input_from_user:
    if i not in l :
        l.append(i)
print("".join(l))

#
ll = [1,2,3,4,5,6,7,8,9]

k = 5
a = k
count = 0
l = []
for i in range(round(len(ll)/5)):
    l.append(ll[count:k])
    k = k + a
    count = count + a

for i in l:
    print(i)
# for i in range(len(ll)):
#     count = count + 1
#     if count == k :
#         print(count)
#         l.append(ll[flag:count])
#         flag = count
#         count = new_flag

print(l)

l = [[1,2,3],[],[4,5],[],[],[6,7,8]]
ll = []
for i in l :
    if i :
        ll.append(i)

print(ll)

str1 = "cwd"
str2 = "crossword"
l1 = [i for i in str1]
l2 = [j for j in str2]
l3 = []
flag = True
for i in str1:
    if i in l2:
        l3.append(l2.index(i))
        l2.remove(i)
    else:
        print("no")
        flag = False
        break
new_list = sorted(l3)
if new_list == l3 and flag:
    print("yes")


l = [[2017,1,1,2017,1,1]]
sm = 1
em = 1
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "octomber", "november","december"]
if sm == em :
    print([months[sm -1 ]])
elif sm < em :
    print(months[sm-1 : em -1])

#
# Given two strings a and b consisting of lowercase characters. The task is to check whether two given strings are anagram of each other or not. An anagram of a string is another string that contains same characters, only the order of characters can be different. For example, “act” and “tac” are anagram of each other.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases. Each test case consist of two strings in 'lowercase' only, in a single line.
#
# Output:
# Print "YES" without quotes if the two strings are anagram else print "NO".
#
# Constraints:
# 1 ≤ T ≤ 300
# 1 ≤ |s| ≤ 1016
#
# Example:
# Input:
# 2
# geeksforgeeks forgeeksgeeks
# allergy allergic
#
# Output:
# YES
# NO
#
# Explanation:
# Testcase 1: Both the string have same characters with same frequency. So, both are anagrams.
# Testcase 2: Characters in both the strings are not same, so they are not anagrams.
string  = "geeksforgeeks forgeeksgeeks"
str = "allergy allergic"
# num_tc = int(input("enter no of test cases"))
num_tc = 1
for i in range(num_tc):
    # string = input("enter string to check ")
    d1 = {}
    d2 = {}
    word1, word2 = string.split()
    for i in word1:
        if i not in d1:
            d1.update({i: word1.count(i)})
    for i in word2:
        if i not in d2:
            d2.update({i: word2.count(i)})
    if d1 == d2 :
        print("YES")
    else:
        print("NO")

# Given a string, the task is to remove duplicates from it. Expected time complexity O(n) where n is length of input string and extra space O(1) under the assumption that there are total 256 possible characters in a string.
#
# Note: that original order of characters must be kept same.
#
# Input:
# First line of the input is the number of test cases T. And first line of test case contains a string.
#
# Output:
# Modified string without duplicates and same order of characters.
#
# Constraints:
# 1 <= T <= 15
# 1 <= |string|<= 1000
#
# Example:
# Input:
# 2
# geeksforgeeks
# geeks for geeks
#
# Output:
# geksfor
# geks for

str  = "geeks for geeks"
l = []
for i in str:
    if i not in l :
        l.append(i)
print("".join(l))

# Given a string S, find length of the longest substring with all distinct characters.  For example, for input "abca", the output is 3 as "abc" is the longest substring with all distinct characters.
#
# Input:
# The first line of input contains an integer T denoting the number of test cases.
# The first line of each test case is String str.
#
# Output:
# Print length of smallest substring with maximum number of distinct characters.
# Note: The output substring should have all distinct characters.
#
# Constraints:
# 1 ≤ T ≤ 100
# 1 ≤ size of str ≤ 10000
#
# Example:
# Input:
# 2
# abababcdefababcdab
# geeksforgeeks
#
# Output:
# 6
# 7

str = "aldshflasghdfasgfkhgasdfasdgvfyweofyewyrtyefgv"
l1 = []
l2 = []
for i in str:
    if i in l2:
        l1.append(len(l2))
        print(l2)
        l2 = []
    else:
        l2.append(i)
print(max(l1))




l = [1,2,3,1,1,6,1,1, 5,6,7,8,1,1,1,1]
# 8
# 7

#--
# 6

# for i in l:
#     print("gg")
#     print(i)
#     l.remove(1)
#     print(l)
# print(l)


a = [1,2,3]
print("ddd")
for a[-1] in a:
    print(a[-1])

x = [1,1,1]
y = x.count(1)
print(y)
x.append(1)
y = x.count(1)
print((y))


inf_empdata = {11:0,22:0,33:0}
x =inf_empdata.keys()
print(len(x))
inf_empdata[77] = 0
print(len(x))


# dictionary comprehenssion
# lsit comprehension

# l = [1,5,6,1,2,4,2]
# # d =  {1:2, 5:1,....}
# d = {}
# for i in l:
#     if i not in d:
#         d[i] = l.count(i)
# # print(d)


# 5 3 logical question
#
# 5 -- 3 --2
# 5 -- 3 -- -1
# 5 -- 3 -- 4
#
# 4

# l1 =[1,0,0,1,1,0,1,0,1]
# # 1 1 1 1 1 = 5
# count = 0
# initial_value = l1[0]
# for i in range(1, len(l1)):
#     if l1[i] != initial_value:
#         count = count + 1
#         initial_value = l1[i]
#     else:
#         initial_value = l1[i]
#
# print(count)


# fd1 = open("sample.txt", "r")
# fd2 = open("hello.txt", "w")
# lines = fd1.readlines()
# for line in lines:
#     if len(line) > 1 and line != "\n":
#         fd2.write(line)
#         fd2.write("\n")
# fd1.close()
# fd2.close()

# list = [break if i%2 == 0 else x  for x in range(10, 50) for i in range(2,x)]
# print(list)
# # l2  = []
# # for i in range(10):
# #     if :
# #         l2.append()
















