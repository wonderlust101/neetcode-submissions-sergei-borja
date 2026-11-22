class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        big = [0] * len(nums)
        small = [0] * len(nums)
        big[0] = small[0] = nums[0]

        for i in range(1, len(nums)):
            candidates = (big[i - 1] * nums[i], small[i - 1] * nums[i], nums[i])
            big[i], small[i] = max(candidates), min(candidates)
        
        return max(big)
