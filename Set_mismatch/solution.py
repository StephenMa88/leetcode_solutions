# attemped in 2021
# 5552ms 15.7 MB
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nnums = sorted(nums)
        dfound = False
        ve = False
        for i, x in enumerate(nnums):
            try:
                try:
                    print(i)
                    if i != 0:
                        if nnums.index(i):
                            pass
                except ValueError:
                    print("VE is {}".format(i))
                    ve = True
                    miss = i
                print(x)
                if x == nnums[i+1]:
                    print("dupe is {}".format(x))
                    dupe = x
                    dfound = True
            except IndexError:
                # finished going through loop
                if dfound and ve:
                    return [dupe, miss]
                try:
                    if nnums.index(dupe+1):
                        print("b exist")
                except ValueError:
                    return [dupe, dupe+1]
                
                try:
                    if nnums.index(dupe-1):
                        print("s exist")
                except ValueError:
                    return [dupe-1, dupe]
                
                return [dupe, len(nums)]
