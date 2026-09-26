class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numSet = set(nums)

        for num in numSet:
            if not num - 1 in numSet:
                count = 1
                while count + num in numSet:
                    count += 1
                res = max(res, count)
            
        return res
        