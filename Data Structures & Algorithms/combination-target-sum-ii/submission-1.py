class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def go(start, remaining):
            if remaining == 0:
                res.append(path[:])

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                path.append(candidates[i])
                go(i + 1, remaining - candidates[i])
                path.pop()

        go(0, target)
        return res
