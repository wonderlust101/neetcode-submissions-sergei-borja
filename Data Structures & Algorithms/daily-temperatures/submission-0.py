class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            highestPos = 0
            for j in range(i, len(temperatures) - 1):
                if temperatures[i] < temperatures[j]:
                    highestPos = j
                    break
            
            res.append(highestPos - i if highestPos > i else 0)
        
        return res
