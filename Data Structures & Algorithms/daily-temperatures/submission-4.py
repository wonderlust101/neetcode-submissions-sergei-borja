class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp_stack = [] # [index, temp]
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while temp_stack and temp_stack[-1][1] < t:
                idx, temp = temp_stack.pop()
                res[idx] = i - idx

            temp_stack.append([i, t])

        return res