class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        seats = [False] *  len(nums)

        def go():
            if len(path) == len(nums):
                res.append(path[:])

            for i in range(len(nums)):
                if seats[i] == False:
                    path.append(nums[i])
                    seats[i] = True
                    go()
                    path.pop()
                    seats[i] = False
            
        go()
        return res
