class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0

        for n in numsSet:
            if not n - 1 in numsSet:
                count = 0
                while n + count in numsSet:
                    count += 1
                
                res = max(res, count)
        
        return res