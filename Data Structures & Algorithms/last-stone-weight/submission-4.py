from _heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]

        heapify(heap)

        while len(heap) > 1:
            x = -heappop(heap)
            y = -heappop(heap)

            if x != y:
                heappush(heap, -(x - y))
        
        return -heap[0] if heap else 0