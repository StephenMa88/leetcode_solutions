# attempted in 2021
# brute force
# 48 ms, 14.2 MB
class Solution:
    def intToRoman(self, num: int) -> str:
        """
        roman_dict = {
            1 : "I",
            5 : "V",
            10 : "X",
            50 : "L",
            100 : "C",
            500 : "D",
            1000 : "M"
        }  
        """     
        
        total = ""
        # take care of thousand digit
        if num >= 1000:
            total = total + str("M" * int(str(num)[0]))
            num = int(str(num)[1:])

        # take care of hundreds digit
        if num >= 900:
            total = total + "CM"
            num = int(str(num)[1:])
        elif num >= 500:
            total = total + "D" + ("C" * (int(str(num)[0]) - 5))
            num = int(str(num)[1:])
        elif num >= 400:
            total = total + "CD"
            num = int(str(num)[1:])
        elif num >= 100:
            total = total + ("C" * (int(str(num)[0])))
            num = int(str(num)[1:])


        # take care of tens digit
        if num >= 90:
            total = total + "XC"
            num = int(str(num)[1:])
        elif num >= 50:
            total = total + "L" + ("X" * (int(str(num)[0]) - 5))
            num = int(str(num)[1:])
        elif num >= 40:
            total = total + "XL"
            num = int(str(num)[1:])
        elif num >= 10:
            total = total + ("X" * (int(str(num)[0])))
            num = int(str(num)[1:])

        # take care of ones digit
        if num == 9:
            total = total + "IX"
        elif num >= 5:
            total = total + "V" + ("I" * (int(str(num)[0]) - 5))
        elif num == 4:
            total = total + "IV"
        elif num >= 1:
            total = total + ("I" * (int(str(num)[0])))
            
        return total
         
