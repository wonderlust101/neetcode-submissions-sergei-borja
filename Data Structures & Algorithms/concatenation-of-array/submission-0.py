class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        tempArr = nums

        for i in range(len(nums)):
            nums.insert(-1, nums[i - 1])

        return tempArr