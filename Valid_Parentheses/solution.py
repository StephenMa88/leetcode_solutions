# attempted in 2021
# 44ms, 14.5 MB
class Solution:
    def __init__(self):
        self.count = 0
        self.valid = {
            "[" : "]",
            "{" : "}",
            "(" : ")"
        }
                 
    
    def isValid(self, s: str) -> bool:
        if s[0] not in "{([" or len(s)%2 != 0:
            return False
        
        other_side = []
        for x in s:
            #if its an opener, we want to append the closer
            if x in "{([":
                other_side.append(self.valid[x])
                print("o {}".format(self.valid[x]))
            elif x not in other_side:
                # if closer can't be found in list, that means it doesn't match opener
                return False
            elif x in "})]" and x == other_side[-1]:
                print("pop {}".format(other_side[-1]))
                other_side.pop()
            else:
                return False
                
        if len(other_side) > 0:
            return False
        return True

# attempt in 2020
# 40ms, 13.9 MB
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if s == "":
            return True
        
        validvars = {
            "(":")",
            "{":"}",
            "[":"]"
        }
        
        inputs = []
        for x in s:
            if validvars.get(x):
                inputs.append(x)
            elif len(inputs) >= 1 and validvars[inputs[-1]] == x:
                inputs.pop()
            else:
                return False
        
        if len(inputs) == 0:
            return True
        else:
            return False
"""
