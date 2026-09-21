class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        bucket = [[] for i in range(len(nums))]

        for n, c in count.items():
            bucket[c - 1].append(n)
        
        res = []

        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                res.append(n)
                
                if len(res) == k:
                    return res
