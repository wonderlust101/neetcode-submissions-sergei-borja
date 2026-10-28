class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # Holds idx
        res = []

        for r, n in enumerate(nums):
            while q and nums[q[-1]] < n:
                q.pop()
            q.append(r)

            if r - k == q[0]:
                q.popleft()
            
            if r + 1 >= k:
                res.append(nums[q[0]])
            
        return res