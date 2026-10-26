class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in numSet:
            if not n - 1 in numSet:
                count = 1
                while count + n in numSet:
                    count += 1
                res = max(res, count)
        
        return res