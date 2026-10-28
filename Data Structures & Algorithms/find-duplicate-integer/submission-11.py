class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0, 0

        while True:
            fast, slow = nums[nums[fast]], nums[slow]

            if fast == slow:
                break
        
        slow2 = 0
        while True:
            slow, slow2 = nums[slow], nums[slow2]

            if slow == slow2:
                return slow