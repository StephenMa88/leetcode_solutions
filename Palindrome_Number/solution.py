# attempt in 2021
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            new_list = [] 
            for v in str(x):
                new_list.append(v)
            if new_list == new_list[::-1]:
                return True
            else:
                return False

# attempt in 2020
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new_str = ""
        l_x = [y for y in str(x)]
        for z in l_x[::-1]:
            new_str += z
        if x == int(new_str):
            return True
        
        return False
"""
