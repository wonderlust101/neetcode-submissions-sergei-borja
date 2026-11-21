class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_helper(houses):
            oneBack, twoBack = 0, 0

            for n in houses:
                oneBack, twoBack = max(oneBack, twoBack + n), oneBack
            
            return oneBack
        
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))