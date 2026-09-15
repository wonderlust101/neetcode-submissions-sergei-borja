class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        num_set = set(nums)

        for i in num_set:
            if (i - 1) not in num_set:
                count = 1
                while i + count in num_set:
                    count += 1
                res = max(res, count)

        return res