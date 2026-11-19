class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)

        if len(s3) != n + m:
            return False

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    continue

                k = i + j - 1
                
                from_a = i > 0 and dp[i - 1][j] and s1[i - 1] == s3[k]
                from_b = j > 0 and dp[i][j - 1] and s2[j - 1] == s3[k]
                dp[i][j] = from_a or from_b
        
        return dp[n][m]