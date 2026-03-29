class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for i, num in enumerate(nums_set):
            if (num - 1 not in nums_set):
                length = 1
                while (num + length) in nums_set:
                    length += 1

                longest = max(longest, length)    
        
        return longest

            