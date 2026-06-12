class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {} # num, index

        # if the diff in the hash, return the diff and num, else put the num in the hash

        for i, n in enumerate(nums):
            diff = target - n 

            if diff in hash:
                return [hash[diff], i]
            
            hash[n] = i

            