class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        res = 0

        for i in numsSet:
            if not i - 1 in numsSet:
                count = 1
                while i + count in numsSet:
                    count += 1
                
                res = max(res, count)
        
        return res