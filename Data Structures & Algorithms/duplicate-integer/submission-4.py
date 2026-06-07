class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numHash = set()

        for i in nums:
            if i in numHash:
                return True
            numHash.add(i)
        
        return False