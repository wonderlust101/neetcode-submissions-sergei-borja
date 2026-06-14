class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_dict = defaultdict(int)
        res = 0
        l = 0

        max_freq = 0
        for r in range(len(s)):
            char_dict[s[r]] += 1
            max_freq = max(char_dict[s[r]], max_freq)

            while (r - l + 1) - max_freq > k:
                char_dict[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res