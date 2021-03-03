# attempted in 2021
# 28 ms, 14.4 MB
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        lstrs = len(strs)
        i = 0

        if strs == [] or strs[0] == "":
            return ""
        for x in strs[0]:
            try:
                #print(x)
                yes_v = 0
                for y in strs:
                    #print(y[i])
                    if y[i] == x:
                        yes_v += 1
                if yes_v == lstrs:
                    prefix += x
                else:
                    return prefix
                i += 1
            except IndexError:
                return prefix
        
        return prefix
# attempted in 2020
# 32ms, 13.9 MB
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""        
        l_strs = len(strs)
        
        if l_strs == 0:
            return output
        elif l_strs == 1:
            return strs[0]

        try:
            for i,x in enumerate(strs[0]):
                count = 1
                for y in range(1,l_strs):
                    if x == strs[y][i]:
                        count += 1
                    else:
                        break
                if count == l_strs:
                    output += x
                else:
                    return output
            return output
        except Exception as m:
            return output
"""
