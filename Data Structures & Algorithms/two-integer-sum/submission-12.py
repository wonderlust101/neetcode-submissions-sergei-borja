class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumHash = {}

        for i, n in enumerate(nums):
            total = target - n

            if total in sumHash:
                return [sumHash[total], i]

            sumHash[n] = i