class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in flights: # U = From, V = To, W = Cost
            graph[u].append((v, w))
        
        fewest = {}
        pile = [(0, src, 0)] # Price, City, Flights Used

        while pile:
            price, city, used = heapq.heappop(pile)

            if city == dst:
                return price
            
            if used == k + 1 or fewest.get(city, float("inf")) <= used:
                continue # Out of flights or no better than an earlier pull
            
            # Updates used
            fewest[city] = used

            # Add other dst to pile
            for nxt, w in graph[city]:
                heapq.heappush(pile, (price + w, nxt, used + 1))
        
        return -1