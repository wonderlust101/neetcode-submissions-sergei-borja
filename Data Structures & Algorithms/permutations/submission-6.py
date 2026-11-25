class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        chairs = [False] * len(nums)

        def dfs():
            if len(path) == len(nums):
                res.append(path[::])
                return

            for i in range(len(nums)):
                if chairs[i]:
                   continue
                
                chairs[i] = True
                path.append(nums[i])
                dfs()
                path.pop()
                chairs[i] = False
        
        dfs()
        return res