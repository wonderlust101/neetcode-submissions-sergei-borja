class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_helper(houses):
            one_back, two_back = 0, 0

            for money in houses:
                one_back, two_back = max(one_back, two_back + money), one_back
        
            return one_back
        
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))