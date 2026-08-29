class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_hash = set()

        for i in nums:
            if i in nums_hash:
                return True
            
            nums_hash.add(i)

        return False