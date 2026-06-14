class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        min_stack = [] # index, temp

        for i, t in enumerate(temperatures):
            while min_stack and min_stack[-1][1] < t:
                idx, temp = min_stack.pop()
                res[idx] = i - idx

            min_stack.append([i, t])
        
        return res