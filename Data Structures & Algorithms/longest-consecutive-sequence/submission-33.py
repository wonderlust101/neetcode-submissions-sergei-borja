class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0

        for n in numsSet:
            if n - 1 not in numsSet:
                count = 1
                while n + count in numsSet:
                    count += 1
                res = max(res, count)
        
        return res