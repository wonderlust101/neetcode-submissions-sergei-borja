class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in range(0, len(nums) - 1):
            if nums[i] == val:
                nums[i].pop()
        
        return nums
