class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        minStack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while minStack and t > minStack[-1][1]:
                stackI, stackT = minStack.pop()
                res[stackI] = i - stackI

            minStack.append([i,t])
        
        return res