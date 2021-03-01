# attempt in 2021
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" and haystack == "" or needle == "":
            return 0
        elif needle == "" or haystack == "":
            return -1
        elif needle in haystack:
            for i, x in enumerate(haystack):
                if x == needle[0]:
                    j = i
                    count = 0
                    for y in needle:
                        if haystack[j] == y:
                            count += 1
                            j += 1
                    print(count)
                    if count == len(needle):
                        return i
        else:
            return -1

# attempt in 2020
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        return haystack.find(needle)
"""
