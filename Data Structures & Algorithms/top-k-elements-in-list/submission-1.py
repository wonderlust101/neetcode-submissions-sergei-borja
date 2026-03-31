class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)

        for num, numCount in count.items():
            freq[numCount].append(num)

        res = []
        for i in range(len(nums), -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res
