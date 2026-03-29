class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in (len(nums) - 1, 0, -1):
            if (nums[i] != val):
                nums.pop(i)

        print(nums)
        

