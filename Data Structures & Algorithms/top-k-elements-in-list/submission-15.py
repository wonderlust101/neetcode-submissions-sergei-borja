class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        bucket = [[] for _ in range(len(nums) + 1)]

        for n in nums:
            num_freq[n] += 1
        
        for val, freq in num_freq.items():
            bucket[freq].append(val)

        res = []
        for i in range(len(bucket) - 1, -1, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res