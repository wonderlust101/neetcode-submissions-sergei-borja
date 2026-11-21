class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need, have = collections.Counter(t), defaultdict(int)
        checked, total = 0, len(need)
        best_tail, tail = float("inf"), 0
        
        l = 0
        for r in range(len(s)):
            have[s[r]] += 1

            if s[r] in need and need[s[r]] == have[s[r]]:
                checked += 1

            while checked == total:
                if r - l + 1 < best_tail:
                    best_tail, tail = r - l + 1, l
                
                have[s[l]] -= 1

                if s[l] in need and need[s[l]] - 1 == have[s[l]]:
                    checked -= 1
                
                l += 1
        
        return "" if best_tail == float("inf") else s[tail: tail + best_tail]