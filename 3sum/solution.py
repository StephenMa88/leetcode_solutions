# attempted in 2021
# 6265ms , 17.4 MB
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        # sort the list
        nums.sort()
        output = []
        
        # first number of the triplet
        for x in range(len(nums)):
            # first num after starter and last num, 2nd and 3rd num of the triplet
            l , r = x+1, len(nums)-1
            # Stop when the index overlap
            while l < r:
                target = nums[x] + nums[l] + nums[r]
                if target == 0:
                    if [nums[x],nums[l],nums[r]] not in output:
                        output.append([nums[x],nums[l],nums[r]])
                    l += 1
                elif target < 0:
                    l += 1
                elif target > 0:
                    r -= 1
        
        return output
