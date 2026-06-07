class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_set = {}

        for i in range(len(nums)):
            diff = target - nums[i]

            if nums[i] in num_set:
                return [num_set[nums[i]], i]

            num_set[diff] = i