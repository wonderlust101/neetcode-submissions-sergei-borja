class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for w in strs:
            word_freq = [0] * 26

            for l in w:
                word_freq[ord(l) - ord('a')] += 1
        
            res[tuple(word_freq)].append(w)
        
        return list(res.values())