class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True] + ([False] * len(s))

        for i in range(len(s) + 1):
            for word in wordDict:
                j = i - len(word)

                if j >= 0 and dp[j] and s[j : i] == word:
                    dp[i] = True
                    break
        print(dp)
        return dp[len(s)]