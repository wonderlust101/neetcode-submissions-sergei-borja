class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_hash = defaultdict(list)

        for w in strs:
            letter_freq = [0] * 26
            for l in w:
                letter_freq[ord(l) - ord('a')] += 1
            
            word_hash[tuple(letter_freq)].append(w)
        
        return list(word_hash.values())