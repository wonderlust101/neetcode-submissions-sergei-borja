class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fp, sp = nums[0], nums[0]

        while True:
            sp, fp = nums[sp], nums[nums[fp]]

            if sp == fp:
                break
        
        sp2 = nums[0]
        while sp != sp2:
            sp, sp2 = nums[sp], nums[sp2]
        
        return sp