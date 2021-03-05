# attempted in 2021
# 36ms 14.2 MB
class Solution:
    def reverse(self, x: int) -> int:
        # reverse it
        y = str(x)[::-1]
        # if negative
        if x < 0:
            y = int("-{}".format(y[:-1]))
        
        
        if int(y) > ((2**31) - 1) or int(y) < -2**31:
            return 0
        else:
            return int(y)

# attempted in 2020
# 32ms 13.8 MB
"""
class Solution:

    def reverse(self, x: int) -> int:
        list_x = []
        n_x = ""
        try:
            is_negative = False
            if x < 0:
                is_negative = True
                x *= -1
            for y in str(x):
                list_x.append(y)
            for i, z in enumerate(list_x[::-1]):
                if i == 0 and z == 0:
                    continue
                n_x += str(z)
            n_x = int(n_x)
            if is_negative:
                n_x *= -1
            
            # need to check if 32 bit int
            if not(int(abs(n_x))>>31):
                return n_x    
            else:
                return 0
        except ValueError:
            return 0
"""
