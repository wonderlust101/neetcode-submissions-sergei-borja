class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        freq = [[] for _ in range(len(nums))]

        for v, c in counts.items():
            freq[c - 1].append(v)
        
        res = []

        for i in range(len(freq) - 1, -1, -1):
            for val in freq[i]:
                res.append(val)

                if len(res) == k:
                    return res