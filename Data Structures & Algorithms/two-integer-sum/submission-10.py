class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumHash = {}

        for i, num in enumerate(nums):
            sum = target - num
            
            if sum in sumHash:
                return [sumHash[sum], i]

            sumHash[num] = i
        