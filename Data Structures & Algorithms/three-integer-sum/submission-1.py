class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            lp = i + 1
            rp = len(nums) - 1

            while lp < rp:
                threeSum = a + nums[lp] + nums[rp]
                if threeSum > 0:
                    rp -= 1
                elif threeSum < 0:
                    lp += 1
                else:
                    res.append([a, nums[lp], nums[rp]])

                    lp += 1
                    while nums[lp] == nums[lp - 1] and lp < rp:
                        lp += 1

        return res