# binary search

def test_location(cards, query, mid):
    if cards[mid] == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return "left"
        else:
            return "found"
    elif cards[mid] < query:
        return "left"
    else:
        return "right"


def locate_card(cards, query):
    # print("cards {} : query {}".format(cards, query))
    low, high = 0, len(cards)-1

    while low <= high:
        mid = (low + high) // 2

        result = test_location(cards, query, mid)
        print("low {} high {} mid {} result {} ".format(low, high, mid, result))
        if result == "found":
            return mid
        elif result == "left":
            high = mid - 1
        elif result == "right":
            low = mid + 1
    return -1


out = list(range(0, 10000))

print(locate_card(out, query=10))

# print(out)

# finding no of rotations of given rotated sorted list with minimum effort
sorted_list = [3, 5, 7, 8, 9] # after rotating 2 times [8, 9, 3, 5, 9]


def count_rotations_linear(nums):
    position = 0
    while position < len(nums):
        if position > 0 and nums[position] < nums[position-1]:
            return position
        position += 1
    return 0


print(count_rotations_linear([8, 9, 3, 5]))


