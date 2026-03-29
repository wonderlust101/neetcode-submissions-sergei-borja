class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i in nums:
            if (nums[i] != val):
                nums.pop(i)

        print(nums)
        

