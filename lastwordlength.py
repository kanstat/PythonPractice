# Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

# A word is a maximal substring consisting of non-space characters only.


# Example 1:

# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.
# Example 2:

# Input: s = "   fly me   to   the moon  "
# Output: 4
# Explanation: The last word is "moon" with length 4.
# Example 3:

# Input: s = "luffy is still joyboy"
# Output: 6
# Explanation: The last word is "joyboy" with length 6.


# count = 0
# s = "luffy is still joyboy"
# for i in s[::-1]:
#     count = count+1
#     if i == ' ':
#         break
# print(count-1)

def wordlength(s):
    count = 0
    s = s.strip()
    for i in s[::-1]:
        count = count+1
        if i == ' ':
            break
    else:
        return count
    count = count-1
    return count


print(wordlength(s="   fly me   to   the moon  "))
