class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_range(lo, hi):
            two_back, one_back = 0, 0

            for i in range(lo, hi + 1):
                two_back, one_back = one_back, max(one_back, two_back + nums[i])
            
            return one_back
        
        return max(rob_range(1, len(nums) - 1), rob_range(0, len(nums) - 2))