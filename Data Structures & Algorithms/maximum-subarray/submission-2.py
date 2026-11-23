class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMax, subMax = 0, nums[0]

        for i in range(len(nums)):
            if currMax < 0:
                currMax = 0
            
            currMax += nums[i]
            subMax = max(subMax, currMax)

        return subMax