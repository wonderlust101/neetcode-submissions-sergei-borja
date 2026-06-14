class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}

        for i, n in enumerate(nums):
            # get diff of target - num
            diff = target - n

            # if diff is in num_dict, return index
            if diff in num_dict:
                return [num_dict[diff], i]
            
            num_dict[n] = i
        
        