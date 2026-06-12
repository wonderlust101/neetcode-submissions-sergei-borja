class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            letter_freq = [0] * 26

            for l in word:
                letter_freq[ord(l) - ord('a')] += 1
            
            res[tuple(letter_freq)].append(word)
        
        return list(res.values())