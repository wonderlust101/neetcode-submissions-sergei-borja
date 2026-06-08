class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        largest_seq = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                seq = 1
                current_num = num

                while current_num + 1 in nums_set:
                    seq += 1
                    current_num += 1
                
                largest_seq = max(largest_seq, seq)

        return largest_seq