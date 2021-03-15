# attempted in 2021
# 32ms, 14.3 MB 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #convert list to num
        num = ""
        for x in digits:
            num = num + str(x)
        
        new_digits = []
        for y in str(int(num) + 1):
            new_digits.append(y)
        
        return new_digits
