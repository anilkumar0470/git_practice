# find a non-empty sub array with largest sum

nums = [4,-1,2,-7,3,4]

def brute_force1():
    max_sum = nums[0]
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum = curr_sum + nums[j]
            max_sum = max(curr_sum, max_sum)
    return max_sum

print(brute_force1())










# time complexity is o(n2)
def brute_force(nums):
    max_sum = nums[0]
    for i in range(len(nums)):
        curr_sum = 0
        for j in range(i, len(nums)):
            curr_sum = curr_sum + nums[j]
            max_sum = max(curr_sum, max_sum)
    return max_sum

print(brute_force(nums))
# can we achieve the same 0(n) yes , using kadanes algo
# the algorithm says if sum of sub array is negative , don't consider means
# don't add that sum to next positive value which will reduce the value
# of positive number, instead of adding negative value to positive value
# start calculate the sum from positive value

def kandanes_algo(nums):
    max_sum = nums[0]
    curr_sum = 0
    for n in nums:
        curr_sum = curr_sum + n
        # the below line will implement kandanes algo
        # if current sum is negative number, we are keeping current sum as zero
        curr_sum = max(curr_sum, 0)
        max_sum = max(max_sum, curr_sum)
    return max_sum

print(kandanes_algo(nums))

# same thing we can achieve using sliding window
# it has two points L, R,
# L is left which is always constant and R will move by one position after iteration done
# the elements between L and R are looks like window and
# when ever the curr_sum becomes negative , we will keep as zero according to kandanes
# algo .. in other words we removed that window and moved another window which is nothing
# but sliding window.


def sliding_window(nums):
    max_sum = nums[0]
    curr_sum = 0
    maxL, maxR = 0, 0
    L = 0
    for R in range(len(nums)):
        if curr_sum < 0:
            curr_sum = 0
            L = R
        if curr_sum > max_sum:
            max_sum = curr_sum
            maxL, maxR = L, R
    return [maxL, maxR]


# given an array , return true if there are two elements with in window
# of size k that are equal.

def brute_force_find_duplicate(nums, k):
    for L in range(len(nums)):
        for R in range(L+1, min(len(nums), L+k)):
            if nums[L] == nums[R]:
                return True
    return False

print(brute_force_find_duplicate([1,2,3,2,3,3], 3))
