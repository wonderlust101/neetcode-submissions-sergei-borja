class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i, ch in enumerate(s):
            last[ch] = i
        
        end = 0
        count = 0
        res = []
        for i, ch in enumerate(s):
            end = max(end, last[ch])
            count += 1

            if end == i:
                res.append(count)
                count = 0
        
        return res