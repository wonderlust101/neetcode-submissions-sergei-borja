class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-n for n in nums]
        heapq.heapify(nums)

        curr_val = None
        while k > 0:
            curr_val = heapq.heappop(nums)
            k -= 1
        
        return -curr_val