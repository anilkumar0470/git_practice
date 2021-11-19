#######################
#   *   *   *   *   * #
#   *   *   *   *   * #
#   *   *   *   *   * #
#   *   *   *   *   * #
#   *   *   *   *   * #
#######################
# square
# for j in range(5):
#     for i in range(5):
#         print("*", end="  ")
#     print("")
#######################
#   *
#   *   *
#   *   *   *
#   *   *   *   *
#   *   *   *   *   *
#######################
# increasing triangle
#######################
# for i in range(5):
#     for j in range(i+1):
#         print("*", end=" ")
#     print("")
#   *   *   *   *   *
#   *   *   *   *
#   *   *   *
#   *   *
#   *
# decreasing triangle
# for i in range(5):
#     for j in range(5-i):
#         print("*", end=' ')
#     print("")

# right sided triangle
# space triangle -- decreasing triangle
# * triangle -- increasing triangle
#                       *
#                   *   *
#               *   *   *
#           *   *   *   *
#       *   *   *   *   *
# for i in range(5):
#     for j in range(5-i):
#         print("  ", end="")
#     for k in range(i+1):
#         print("*", end=" ")
#     print("")

# right sided triangle
# increasing space
# decreasing star
# *   *   *   *   *
#     *   *   *   *
#         *   *   *
#             *   *
#                 *

# for i in range(5):
#     for j in range(i+1):
#         print("  ", end='')
#     for k in range(5-i):
#         print("*", end=' ')
#     print("")
######################################
# Hill pattern
#                   *
#               *   *   *
#           *   *   *   *   *
#       *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *
######################################
# for i in range(5):
#     for j in range(5-i):
#         print("  ", end="")
#     for k in range(i+1):
#         print("*", end=" ")
#     for l in range(i):
#         print("*", end=" ")
#     print("")


# reverse hill pattern
#   *   *   *   *   *   *   *   *   *
#       *   *   *   *   *   *   *
#           *   *   *   *   *
#               *   *   *
#                   *
# increase space triangle
# decrease star left side
# decrease star right side
# for i in range(5):
#     for j in range(i+1):
#         print("  ", end="")
#     for k in range(5-i):
#         print("*", end=" ")
#     for l in range(4-i):
#         print("*", end=" ")
#     print("")
# =================================
for i in range(4):
    for j in range(5-i):
        print("  ", end="")
    for k in range(i+1):
        print("*", end=" ")
    for l in range(i):
        print("*", end=" ")
    print("")
for i in range(5):
    for j in range(i+1):
        print("  ", end="")
    for k in range(5-i):
        print("*", end=" ")
    for l in range(4-i):
        print("*", end=" ")
    print("")