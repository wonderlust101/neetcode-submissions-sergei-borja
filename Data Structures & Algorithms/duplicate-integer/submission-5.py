class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_hash = set()

        for num in nums:
            if num in num_hash:
                return True
            num_hash.add(num)

        
        return False