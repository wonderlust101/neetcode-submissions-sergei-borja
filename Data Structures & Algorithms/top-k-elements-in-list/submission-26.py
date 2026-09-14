class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = collections.Counter(nums)
        freqBucket = [[] for i in range(len(nums) + 1)]

        for num, i in countMap.items():
            freqBucket[i].append(num)
        
        res = []

        for i in range(len(freqBucket) - 1, 0, -1):
            for num in freqBucket[i]:
                res.append(num)
                if len(res) == k:
                    return res