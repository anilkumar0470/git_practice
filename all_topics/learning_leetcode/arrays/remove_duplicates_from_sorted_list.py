nums = [1,1,2,3,4,4,4]


def remove_duplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            nums[i+1], nums[j] = nums[j], nums[i+1]
            i += 1
    return i+1


# print(nums[0:remove_duplicates(nums=nums)])


nums1 = [1,2,3,4,4,3,2,1]
outpu = [1,4,2,3,3,2,4,1]
n1 = 4
out = []

for i in range(len(nums1)//2):
    out.append(nums1[i])
    out.append(nums1[n1 + i])
    print(out)
