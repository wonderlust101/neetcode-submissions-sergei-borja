class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def explore(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return 

            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    break
                
                if i > start and candidates[i - 1] == candidates[i]:
                    continue
                
                path.append(candidates[i])
                explore(i + 1, remaining - candidates[i])
                path.pop()
        
        explore(0, target)
        return res