# Given two binary strings a and b, return their sum as a binary string.


# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"

def stringbinary(a: str, b: str):
    sum = bin(int(a, 2)+int(b, 2))

    return sum[2::]


print(stringbinary(a="11", b="1"))
