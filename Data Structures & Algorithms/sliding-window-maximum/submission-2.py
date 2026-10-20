class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # Largest at front (largest index)
        res = []

        for r in range(len(nums)):
            # Pop all numbers smaller than curr val
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            # Append curr vale
            q.append(r)

            # If the largest is out of the window, pop it out
            if q[0] == r - k:
                q.popleft()
            
            # Appened the largest once the max window exists
            if r >= k - 1:
                res.append(nums[q[0]])
        
        return res