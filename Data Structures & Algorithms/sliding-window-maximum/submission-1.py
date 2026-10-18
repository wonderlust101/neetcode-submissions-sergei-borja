class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # Deque with index of the largest being the first always
        res = [] # Result 

        for i in range(len(nums)):
            # Ensure the last val of the q is smaller than the curr val
            while q and nums[q[-1]] <= nums[i]:
                q.pop()

            q.append(i)

            # Remove the first index in queue if pasts the window
            if q[0] == i - k:
                q.popleft()

            # If the window is full, append the first val in the  to the res
            if i >= k - 1:
                res.append(nums[q[0]])

        return res