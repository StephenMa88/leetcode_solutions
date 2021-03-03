# attempt in 2021
# 88ms , 15.9 MB
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
		# continue to loop if I finds a dup
        while True:
            pop = 0
            for i, x in enumerate(nums):
                try:
                    if x == nums[i+1]:
                        nums.pop(i+1)
                        pop += 1
                except IndexError:
                    pass
            if pop == 0:
                return len(nums)

# attempt in 2020
# 96ms, 16 MB
"""
I find it suprising this solution is slower...
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        try:
            for i,x in enumerate(nums):
			# it will keep popping next value as long 
			# as it is equal to x
                while x == nums[i+1]:
                    nums.pop(i+1)
        except:
            return len(nums)
"""
