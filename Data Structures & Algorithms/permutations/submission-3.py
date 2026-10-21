class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        seats = [False] * len(nums)

        def dfs():
            if len(nums) == len(path):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if seats[i] == True:
                    continue
                
                seats[i] = True
                path.append(nums[i])
                dfs()
                
                path.pop()
                seats[i] = False

        dfs()
        return res