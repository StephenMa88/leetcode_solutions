#attempted in 2021 , 53 testcases
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tsum_dict = {}
        for i, x in enumerate(nums):
            if tsum_dict.get(x):
                tsum_dict[x].append(i)
            else:
                tsum_dict[x] = [i]
        for x in nums[::-1]:
            lookup = target - x
            if lookup == x and len(tsum_dict[lookup]) > 1:
                return tsum_dict[x]
            elif tsum_dict.get(lookup) is not None:
                return tsum_dict[x] + tsum_dict[lookup]


# attempted in 2020, 29 test cases
"""
class Solution:
    def twoSum(self, nums: List[int], target: int)-> List[int]:
        """
        Runtime: 1904 ms, faster than 23.03%
        Memory Usage: 15 MB, less than 7.20% 
        indicies = {}
        results = []

        # without hash
        for x in range(len(nums)):
            other_num = target - nums[x]
            if other_num in nums:
                if nums.index(other_num) != x:
                    results.append(x)
                    results.append(nums.index(other_num))
                    return results

        """
        # create a hash table or dictionary to hold all index and value
        #for x in range(len(nums)):
        #    indicies[x] = nums[x]
        # create dict using dict comprehension {2:[0], 7:[1]}
        # Runtime: 76 ms Memory Usage: 16.2 MB
        indi = {}
        for x in range(len(nums)):
            if nums[x] not in indi:
                indi[nums[x]] = [x] 
            else:
                indi[nums[x]].append(x)

        # Loop through the dict.                
        for ind,num in enumerate(nums):
            o_num = target - num
            n_ind = indi.get(o_num)
            if n_ind:
                if len(n_ind) == 1 and n_ind[0] != ind:
                    return [ind, n_ind[0]]
                elif len(n_ind) > 1 :
                    return [ind, n_ind[1]]
"""
