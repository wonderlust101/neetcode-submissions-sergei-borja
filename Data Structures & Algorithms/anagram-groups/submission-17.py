class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for w in strs:
            letterFreq = [0] * 26

            for l in w:
                letterFreq[ord(l) - ord('a')] += 1
            
            res[tuple(letterFreq)].append(w)
        
        return list(res.values())