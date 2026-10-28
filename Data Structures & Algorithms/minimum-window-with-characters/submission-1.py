class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = collections.Counter(t), defaultdict(int)
        ticked, total = 0, len(need)
        best, best_i = float("inf"), 0

        l = 0
        for r in range(len(s)):
            have[s[r]] += 1
            if s[r] in need and need[s[r]] == have[s[r]]:
                ticked += 1
            
            while ticked == total:
                if (r - l + 1) < best:
                    best, best_i = r - l + 1, l
                
                have[s[l]] -= 1
                if  s[l] in need and need[s[l]] - 1 == have[s[l]]:
                    ticked -= 1
                
                l += 1
        
        return "" if best == float("inf") else s[best_i:best_i + best]