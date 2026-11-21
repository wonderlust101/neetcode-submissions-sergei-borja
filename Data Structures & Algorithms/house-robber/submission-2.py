class Solution:
    def rob(self, nums: List[int]) -> int:
        oneBack, twoBack = 0, 0

        for n in nums:
            oneBack, twoBack = max(oneBack, twoBack + n), oneBack
        
        return oneBack