class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ord_map = {} 
        anagrams_groups = []

        for s in strs:
            letter_sum = 0
            for l in s:
                letter_sum += ord(l)
            
            if (letter_sum not in ord_map):
                ord_map[letter_sum] = len(ord_map)

            if len(ord_map) > len(anagrams_groups):
                anagrams_groups.append([s])
            else:
                anagrams_groups[ord_map[letter_sum]].append(s)
            
            
        return anagrams_groups