# attempted in 2021
# 1924ms, 14.5 MB
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        longest = 1
        """
        # with this it can be really fast.
        # but not optimal. 108 ms, 14.1 MB
        if len(s) > 100:
            r = 50
        else:
            r = len(s)
        """
        for j in range(len(s)):
            curr = []
            for i, x in enumerate(s[j:]):
                if i == 0:
                    curr = [x]
                else:
                    if x in curr:
                        curr = [x]
                        break
                    else:
                        curr.append(x)
                if len(curr) > longest:
                    longest = len(curr)
                    #print("{} {}".format(longest, curr))
            if (longest > (len(s[j:]))):
                return longest
        return longest

# attempt in 2020
# 1680ms, 14.1 MB
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        """ This solves up to 407/987. Then it requires log(n)
        n_str = [s[0]]
        output = 0
        for x in range(1,len(s)):
            if s[x] not in n_str:
                n_str.append(s[x])
            else:
                if len(n_str) > output:
                    output = len(n_str)
                n_str = [s[x]]
        if len(n_str) > output:
            output = len(n_str)
        
        return output
        """ 
        output = 0
        n_str = []
        for x,y in enumerate(s):
            n_str.append(y)
            #if x == len(s):
            #    break
            # looks and the smaller list
            for z in range(x+1, len(s)):
                if s[z] not in n_str:
                    n_str.append(s[z])
                else:
                    break
            if len(n_str) > output:
                output = len(n_str)
            n_str = []
            
        return output
"""
B
B
B
B
B
B
B
B
B
B
        return output
