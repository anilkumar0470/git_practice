# # *
# # **
# # ***
# # ****
#
#
# for i in range(5):
#     for j in range(i):
#         print("*", end= " ")
#     print("")
#
# #######################
# #   *   *   *   *   * #
# #   *   *   *   *   * #
# #   *   *   *   *   * #
# #   *   *   *   *   * #
# #   *   *   *   *   * #
# #######################
# # square
# for j in range(5):
#     for i in range(5):
#         print("*", end="  ")
#     print("")
# #######################
# #   *
# #   *   *
# #   *   *   *
# #   *   *   *   *
# #   *   *   *   *   *
# #######################
# # increasing triangle
# #######################
# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print("")
# #   *   *   *   *   *
# #   *   *   *   *
# #   *   *   *
# #   *   *
# #   *
# # decreasing triangle
# for i in range(5):
#     for j in range(5-i):
#         print("*", end=' ')
#     print("")
#
# # right sided triangle
# # space triangle -- decreasing triangle
# # * triangle -- increasing triangle
# #                       *
# #                   *   *
# #               *   *   *
# #           *   *   *   *
# #       *   *   *   *   *
# for i in range(5):
#     for j in range(5-i):
#         print(" ", end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     print("")
#
# # right sided triangle
# # increasing space
# # decreasing star
# # *   *   *   *   *
# #     *   *   *   *
# #         *   *   *
# #             *   *
# #                 *
#
# for i in range(5):
#     for j in range(i+1):
#         print("  ", end='')
#     for k in range(5-i):
#         print("*", end=' ')
#     print("")
######################################
# # Hill pattern
# #                   *
# #               *   *   *
# #           *   *   *   *   *
# #       *   *   *   *   *   *   *
# #   *   *   *   *   *   *   *   *   *
# # ######################################
# for i in range(5):
#     for j in range(5-i):
#         print("  ", end="")
#     for k in range(i+1):
#         print("*", end=" ")
#     for l in range(i):
#         print("*", end=" ")
#     print("")
#
#
# # reverse hill pattern
# #   *   *   *   *   *   *   *   *   *
# #       *   *   *   *   *   *   *
# #           *   *   *   *   *
# #               *   *   *
# #                   *
# # increase space triangle
# # decrease star left side
# # decrease star right side
# for i in range(5):
#     for j in range(i+1):
#         print("  ", end="")
#     for k in range(5-i):
#         print("*", end=" ")
#     for l in range(4-i):
#         print("*", end=" ")
#     print("")
# # =================================
# for i in range(5):
#     for j in range(5-i):
#         print("  ", end="")
#     for k in range(i+1):
#         print("*", end=" ")
#     for l in range(i):
#         print("*", end=" ")
#     print("")
# for i in range(5):
#     for j in range(i+1):
#         print("  ", end="")
#     for k in range(5-i):
#         print("*", end=" ")
#     for l in range(4-i):
#         print("*", end=" ")
#     print("")
#
# for i in range(5):
#     for j in range(i+1):
#         print(i+j, end= " ")
#     print("")

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()

# #######################
# #   *
# #   *   *
# #   *   *   *
# #   *   *   *   *
# #   *   *   *   *   *
# #######################

# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# 1
# 12
# 123
# 1234
# 12345

# for i in range(1,6):
#     for j in range(i+1):
#         print(j, end="")
#     print()

# 1
# 22
# 333
# 4444
# 55555

# for i in range(1, 6):
#     for j in range(i):
#         print(i, end="")
#     print()

# *****
# ****
# ***
# **
# *

# for i in range(5):
#     for j in range(5-i):
#         print("*", end="")
#     print()

# 12345
# 1234
# 123
# 12
# 1
# for i in range(1,6):
#     for j in range(1,7-i):
#         print(j, end="")
#     print()

# # Hill pattern
# #                   *
# #               *   *   *
# #           *   *   *   *   *
# #       *   *   *   *   *   *   *
# #   *   *   *   *   *   *   *   *   *

# for i in range(5):
#     for j in range(5-i):
#         print(" ", end="")
#     for k in range(i+1):
#         print("*", end="")
#     print()
#
# for i in range(10):
#     for j in range(10-i):
#         print("  ", end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     print("")

# for i in range(5):
#     for j in range(5-i):
#         print(" ", end=" ")
#     for l in range(i+1):
#         print("*", end=" ")
#     print()
#
# for i in range(5):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for k in range(5-i):
#         print("*", end=" ")
#     for l in range(k):
#         print("*", end=" ")
#     print()
#
# for i in range(5):
#     for j in range(5-i):
#         print(" ", end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     for l in range(k):
#         print("*", end=" ")
#
#     # for k in range(i+1):
#     #     print("*", end=" ")
#     # for l in range(k):
#     #     print("*", end=" ")
#     print()
# for ii in range(5):
#     for jj in range(5-ii):
#         print(" ", end=" ")
#     for kk in range(ii+1):
#         print("*", end=" ")
#     for ll in range(kk):
#         print("*", end=" ")
#     print()
#
# for i in range(5):
#     for j in range(5-i):
#         print(" ", end=" ")
#     for k in range(i+1):
#         print("*", end=" ")
#     for l in range(k):
#         print("*", end=" ")
#     print()
#
# for ii in range(5):
#     for jj in range(5-ii):
#         print("*", end=" ")
#     for kk in range(jj):
#         print("*", end=" ")
#     for ll in range(kk):
#         print(" ", end=" ")
#     print()

#
# primes = range(2, 20)
# for i in range(2, 8):
#     primes = filter(lambda x: x==i or x%i, primes)
# else:
#     print(list(primes))

# square
# for i in range(5):
#     for j in range(5):
#         print("*", end=" ")
#     print()

# increasing triangle

# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print()

# decreasing triangle
# for i in range(5):
#     for j in range(5-i):
#         print("*", end=" ")
#     print()

# right sided triangle
#                 *
#             *   *
#         *   *   *
#     *   *   *   *
# *   *   *   *   *

# for i in range(5):
#     for j in range(5-i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     print()

# for i in range(5):
#     for k in range(i+1):
#         print(" ", end=" ")
#     for j in range(5-i):
#         print("*", end=" ")
#
#     print()


# for i in range(5):
#     for j in range(5-i):
#         print(" ", end=" ")
#     for k in range(i):
#         print("*", end=" ")
#     for l in range(i+1):
#         print("*", end=" ")
#     print()

# for i in range(5):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for k in range(4-i):
#         print("*", end=" ")
#     for l in range(5-i):
#         print("*", end=" ")
#     print()










# # 0 1 2 3 4
# for i in range(5): # i = 0, 1
#     print(i, end="#") # 0 \n -- new line
#
# for i in range(10): # i =4 rows
#     for j in range(10): # 0-4 j = 0,1,2,3,4 # columns
#         print("*", end=" ")
#     print()

# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

# triangle
# *
# *   *
# *   *   *
# *   *   *   *
# *   *   *   *   *

# for i in range(5): # 0-4 , i = 4
#     for j in range(i+1): # 0 ,  0123,j = 0
#         print("&", end=" ")
#     print()
# *
# * *
# * * *
# * * * *
# * * * * *

# triangle
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(5): # i = 2, 01234
#     for j in range(5-i): # 012 j = 012
#         print("*", end=" ")
#     print()

# for i in range(5):
# 	for j in range(5-i):
# 		print(" ", end=" ")
# 	for k in range(i+1):
# 		print("*", end=" ")
# 	print()

# for i in range(5):
# 	for j in range(i+1):
# 		print(" ", end=" ")
# 	for k in range(5-i):
# 		print("*", end=" ")
# 	print()


















#
# # right sided triangle
# # - - - - *
# # - - - * *
# # - - * * *
# # - * * * *
# # * * * * *
# # spaces are decreasing
# # starts are increasing
#
# for i in range(5): # i = 4
#     for j in range(5-i): # 0 j = 0
#         print(" ", end=" ")
#     for k in range(i+1): # 01234 k=4
#         print("*", end=" ")
#     print()
#
# #         *
# #       * *
# #     * * *
# #   * * * *
# # * * * * *


# left sided triangle
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
# spaces are increasing
# stars are decreasing
#

# for i in range(5):# 01234 i = 4
#     for j in range(i+1):# 01234 j =4
#         print(" ", end=" ")
#     for k in range(5-i):# 0 k = 0
#         print("*", end=" ")
#     print()

#  * * * * *
#    * * * *
#      * * *
#        * *
#          *

#
#     			  *
#             *   *   *
#         *   *   *   *   *
#     *   *   *   *   *   *   *
# *   *   *   *   *   *   *   *   *
# spaces are decreasing
# for i in range(5):# 01234 i = 4
#     for j in range(5-i):# 0 j = 0
#         print(" ", end=" ")
#     for k in range(i):# 0123 k =3
#         print("*", end=" ")
#     for l in range(i+1):# 01234 l = 4
#         print("*", end=" ")
#     print()
#          *
#       *  *  *
#    *  *  *  *  *
#  * *  *  *  *  *  *
#* * *  *  *  *  *  *  *

# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *
# spaces are increasing
# stars are decreasing
# stars are decreasing

# for i in range(5):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for k in range(4-i):
#         print("*", end=" ")
#     for l in range(5-i):
#         print("*", end=" ")
#     print()


