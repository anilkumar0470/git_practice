# Given an array return true if there are two elements within
# window size of k that are equal.
# input : [1,2,3,2,3,4]

# bruteforcce

def close_duplicates_brute_force(nums, k):
    for L in range(len(nums)):
        for R in range(L+1, min(len(nums), L+k)):
            if nums[L] == nums[R]:
                return True
    return False

# print(close_duplicates_brute_force([1,2,3,4,3,3],3))
# the above one is brut force , can we do it one loop
# yes we can achieve the same
# to form the window means we need to use L,R
# L will be 0 and R will be changing
# form the window with given size k
# while add window elements to set check if it is already presented
# if presented return True
# once all elements added,
# remove the L position value from the set
# increment L by 1


def close_duplicates(nums, k):
    window = set()
    L = 0
    for R in range(len(nums)):
        if L - R + 1 > k:
            window.remove(nums[L])
            L = L + 1
        if nums[R] in window:
            return True
        window.add(nums[R])
    return False


# print(close_duplicates([1,2,3,4,5], k=3))

# find the minimum length sub array , where sum is greater
# than or equal to the target, assume all values are positive

def minimum_len_sub(nums, target):
    L, total = 0,0
    for R in range(len(nums)):
        








