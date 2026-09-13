class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsHash = set()

        for i in nums:
            if i in numsHash:
                return True
            numsHash.add(i)
        
        return False