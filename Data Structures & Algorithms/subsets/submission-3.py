class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def explore(start):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                explore(i + 1)
                path.pop()
        
        explore(0)
        return res