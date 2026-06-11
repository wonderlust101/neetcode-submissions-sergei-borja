class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for w in strs:
            letter_hash = [0] * 26
            for l in w:
                letter_hash[ord(l) - ord('a')] += 1
            
            res[tuple(letter_hash)].append(w)
        
        return list(res.values())
