class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dict = defaultdict(list)

        for word in strs:
            letter_freq = [0] * 26
            for l in word:
                letter_freq[ord(l) - ord("a")] +=1
            
            word_dict[tuple(letter_freq)].append(word)

        return list(word_dict.values())