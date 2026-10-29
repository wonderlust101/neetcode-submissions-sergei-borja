class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        used = [False] * len(nums)

        def explore():
            if len(path) == len(nums):
                res.append(path[:])
                return
            
            for i in range(len(nums)):
                if used[i] == True:
                    continue
                
                used[i] = True
                path.append(nums[i])
                explore()
                path.pop()
                used[i] = False
        
        explore()
        return res