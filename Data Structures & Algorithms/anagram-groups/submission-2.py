class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaMap = defaultdict(list)

        for w in strs:
            wordMap = [0] * 26

            for l in w:
                wordMap[ord(l) - ord("a")] += 1
            
            anaMap[tuple(wordMap)].append(w)

        return list(anaMap.values())