class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def explore(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(nums)):
                if nums[i] > remaining:
                    break

                path.append(nums[i])
                explore(i, remaining - nums[i])
                path.pop()
        
        explore(0, target)
        return res