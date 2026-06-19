class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        sp, fp = nums[0], nums[0]

        while True:
            sp = nums[sp]
            fp = nums[nums[fp]]

            if sp == fp:
                break
        
        sp2 = nums[0]
        while True:
            if sp == sp2:
                return sp
            sp = nums[sp]
            sp2 = nums[sp2]

