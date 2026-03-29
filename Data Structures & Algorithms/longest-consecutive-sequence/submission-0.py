class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        res = 1

        nums.sort()

        curr = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                curr += 1
            else:
                res = max(res, curr)
                curr = 1
        
        return max(res, curr)
            