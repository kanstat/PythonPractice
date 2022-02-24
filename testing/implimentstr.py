# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


# Example 1:

# Input: haystack = "helolo", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Example 3:

# Input: haystack = "", needle = ""
# Output: 0

def implmentNeedle(haystack, needle):  # helollo
    if needle == "":
        return 0
    for i in range(0, len(needle)):
        for x in range(0, len(haystack)):
            if haystack[x:x+len(needle)] != needle or haystack == "":
                return -1
            if needle[i] == haystack[x]:
                # print(haystack[x:x+len(needle)])
                if haystack[x:x+len(needle)] == needle:
                    return x


if __name__ == "__main__":
    print(implmentNeedle(haystack="", needle="ooo"))
