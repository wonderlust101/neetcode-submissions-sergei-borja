class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        minStack = [] # [i, t]

        for i, t in enumerate(temperatures):
            while minStack and minStack[-1][1] < t:
                idx, temp = minStack.pop()
                res[idx] = i - idx

            minStack.append([i, t])
        
        return res