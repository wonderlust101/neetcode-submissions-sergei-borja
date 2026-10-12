class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        freq = [[] for i in range(len(nums))]

        for n, c in counts.items():
            freq[c - 1].append(n)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                res.append(n)

                if len(res) == k:
                    return res