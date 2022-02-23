# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl";//
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

def lengthWord(str):
    length = len(str[0])  # 6
    for word in str:
        lenWord = len(word)
        if lenWord < length:
            length = lenWord
    print(length)
    return length


lengthWord(str=["dog", "racecar", "car"])


# def prefixMatch(str):
#     for i in range(len(str)-1):  # 0,1,2
#         for x in range(len(i)):
#             if str[i][x] == str[i+1][x]:
