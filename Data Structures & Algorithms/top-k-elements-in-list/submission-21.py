class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = defaultdict(int)
        buckets = [[] for _ in range(len(nums))]

        # frequency of each number
        for n in nums:
            num_freq[n] += 1

        # {1:1, 2:2, 3:3}

        # bucket sort
        for num, freq in num_freq.items():
            buckets[freq - 1].append(num)
        
        # least        most
        # [[1], [2], [3]]

        res = []
        for bucket in range(len(buckets) - 1, -1, -1):
            for i in buckets[bucket]:
                res.append(i)

                if len(res) == k:
                    return res
