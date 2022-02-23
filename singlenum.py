# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.


# Example 1:

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4
# Example 3:

# Input: nums = [1]
# Output: 1

def singleNum(nums):
    if len(nums) <= 1:
        return nums[0]
    for n in range(len(nums)):  # 0,1,2
        for i in range(len(nums)):  # 0,1,2
            if n == i:
                continue
            if nums[n] == nums[i]:
                break
        else:
            return nums[n]


if __name__ == "__main__":
    print(singleNum(nums=[2, 2, 1, 1, 3, 3, 6, 7, 7]))
