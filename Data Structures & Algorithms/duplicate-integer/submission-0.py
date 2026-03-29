class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_values = set()

        for i in nums:
            if i in unique_values:
                return True
            else:
                unique_values.add(i)
        
        return False