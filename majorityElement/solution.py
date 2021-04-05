# Attempted in 2021
# 172 ms, 15.4 MB
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
		# sort the list of numbers
        nums.sort()
        
        maxn = 0
        maxc = 0
        curn = nums[0]
        curc = 1
        
        for x in nums[1:]:
            if x == curn:
                curc += 1
            elif x != curn:
                if curc > maxc:
                    maxn = curn
                    maxc = curc
                    curn = x
                    curc = 1
                else:
                    curn = x
                    curc = 1
        if curc > maxc:
            return curn
        else:
            return maxn
            
