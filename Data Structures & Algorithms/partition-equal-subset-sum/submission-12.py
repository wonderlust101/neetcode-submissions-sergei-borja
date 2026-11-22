class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)

        if total % 2:
            return False

        target = total // 2

        dp = [True] + ([False] * total)
        
        for n in nums:
            for i in range(target, -1, -1):
                if dp[i - n] or dp[i]:
                    dp[i] = True

                if dp[target]:
                    break
        
        return dp[target]
            
