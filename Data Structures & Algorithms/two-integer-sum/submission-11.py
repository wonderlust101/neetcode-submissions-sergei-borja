class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        valHash = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in valHash:
                return [valHash[diff], i]

            valHash[num] = i
