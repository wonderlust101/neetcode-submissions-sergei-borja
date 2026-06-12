class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_hash = set(nums)
        res = 0
        # 1,2,3,4,5,6,20,30

        for num in num_hash:
            if num - 1 not in num_hash:
                length = 1
                while num + length in num_hash:
                    length += 1
                
                res = max(res, length)

        return res