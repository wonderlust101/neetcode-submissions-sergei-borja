class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSet = set(nums)

        for num in numsSet:
            if not num - 1 in numsSet:
                count = 1
                while num + count in numsSet:
                    count += 1
                res = max(res, count)
        
        return res

