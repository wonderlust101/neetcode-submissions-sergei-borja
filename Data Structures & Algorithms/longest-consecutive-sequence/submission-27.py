class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        res = 0

        for n in numset:
            if not n - 1 in numset:
                count = 1
                while count + n in numset:
                    count += 1
                res = max(res, count)
        
        return res