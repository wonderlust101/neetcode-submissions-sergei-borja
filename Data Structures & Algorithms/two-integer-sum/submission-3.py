class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {} # diff, idx

        for i, val in enumerate(nums):
            diff = target - val

            if diff in sumMap:
                return [sumMap[diff], i]
            
            sumMap[val] = i