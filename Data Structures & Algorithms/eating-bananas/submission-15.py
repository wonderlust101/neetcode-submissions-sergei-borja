class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_k = max(piles)

        while l <= r:
            m = (l + r) // 2

            time = 0
            for pile in piles:
                time += math.ceil(pile / m) 
            
            if time <= h:
                r = m - 1
                min_k = min(min_k, m)
            else:
                l = m + 1
        
        return min_k
            
