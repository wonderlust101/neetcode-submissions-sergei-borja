class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            counts = [0] * 26

            for l in s:
                counts[ord(l) - ord('a')] += 1
            
            res[tuple(counts)].append(s)
        
        return list(res.values())