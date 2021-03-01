class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #if len(nums) == 1 and target == 1:
        #    return 0

        # create a dict out of the list
        search_dict = {}
        for i,x in enumerate(nums):
            search_dict[x]=i
            
        if search_dict.get(target) != None:
            #print(search_dict)
            return search_dict[target]
        else:
            # long way
            nums.append(target)
            new_list = sorted(nums)
            search_dict = {}
            for i,x in enumerate(new_list):
                search_dict[x]=i
            return search_dict[target]
