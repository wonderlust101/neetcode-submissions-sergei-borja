class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # {difference, index}
        prevMap = {}

        for i, value in enumerate(nums):
            diff = target - value

            if diff in prevMap:
                return [prevMap[diff], i]

            prevMap[value] = i