class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsHash = {}

        for i in nums:
            if i in numsHash:
                return True
            numsHash[i] = 1
        
        return False