# attempted in 2021
# 64ms, 15.4 MB
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curn = fn = nums[0] # curr num and final num
        if len(nums) == 1:
            return nums[0]
        
        for x in range(1, len(nums)):
            #print("%s ? %s" % (0, nums[x] + curn))
            curn = max(nums[x], nums[x]+curn)
            
            #print("%s ? %s" % (fn,curn))
            fn = max(fn, curn)
            print(fn)
        
        return fn
