class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def explore(start):
            res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                
                path.append(nums[i])
                explore(i + 1)
                path.pop()
        
        explore(0)
        return res