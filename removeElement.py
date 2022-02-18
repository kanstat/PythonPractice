# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).

def removeElement(nums, val: int) -> int:
    count = 0
    for i in range(len(nums)):
        if val == nums[i]:

            count = count+1
    total_len = len(nums)
    try:
        while True:
            nums.remove(val)
    except:
        pass
    return total_len - count
