# attempt in 2021
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # reversing the list will make it so that an index is filled when popped
        for x in nums[::-1]:
            #print("val: {}".format(x))
            if x == val:
                #print(x)
                nums.remove(x)

        return len(nums)

# attempt in 2020
# shorter lines, but since it needs to repeat it would take longer if big cases
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while nums.count(val) != 0:
            nums.pop(nums.index(val))
        return
"""
