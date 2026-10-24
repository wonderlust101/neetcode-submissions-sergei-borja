class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = collections.Counter(t), defaultdict(int)
        checked, total = 0, len(need)
        best, best_idx = float("inf"), 0

        l = 0

        for r, c in enumerate(s):
            have[c] += 1

            if c in need and have[c] == need[c]:
                checked += 1
            
            while checked == total:
                if (r - l + 1) < best:
                    best, best_idx = r - l + 1, l
                
                oldC = s[l]
                have[oldC] -= 1

                if oldC in need and have[oldC] == need[oldC] - 1:
                    checked -= 1
                
                l += 1
        
        return s[best_idx:best_idx + best] if best != float("inf") else ""