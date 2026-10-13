class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSet = set(nums)

        for n in numsSet:
            if not n - 1 in numsSet:
                count = 1
                while count + n in numsSet:
                    count += 1
                res = max(res, count)
        
        return res