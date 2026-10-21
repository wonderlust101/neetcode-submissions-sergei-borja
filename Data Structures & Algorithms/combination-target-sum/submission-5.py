class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def dfs(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            
            for i in range(start, len(nums)):
                if remaining < nums[i]:
                    break
                
                path.append(nums[i])
                dfs(i, remaining - nums[i])
                path.pop()
        
        dfs(0, target)
        return res