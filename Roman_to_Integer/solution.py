# attempted in 2021
class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        total = 0
        for i, x in enumerate(s):
            total += roman_dict[x]
            if i != 0:
                if x in "VX" and s[i-1] == "I":
                    total -= 2
                if x in "LC" and s[i-1] == "X":
                    total -= 20
                if x in "DM" and s[i-1] == "C":
                    total -= 200
            print(total)
        return total

