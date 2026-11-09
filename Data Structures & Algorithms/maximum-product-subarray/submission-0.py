class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        big = [0] * n
        small = [0] * n
        big[0] = small[0] = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            candidates = (big[i - 1] * x, small[i - 1] * x, x)
            big[i], small[i] = max(candidates), min(candidates)
        
        return max(big)