class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0

        while True:
            slow, fast = nums[slow], nums[nums[fast]]

            if slow == fast:
                break
        
        slowD = 0

        while True:
            slow, slowD = nums[slow], nums[slowD]

            if slow == slowD:
                return slow