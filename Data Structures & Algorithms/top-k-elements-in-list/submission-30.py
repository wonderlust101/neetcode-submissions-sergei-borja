class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        buckets = [[] for i in range(len(nums))]

        for i, c in counts.items():
            buckets[c - 1].append(i)
        
        res = []

        for b in range(len(buckets) - 1, -1, -1):
            for i in buckets[b]:
                res.append(i)

                if len(res) == k:
                    return res