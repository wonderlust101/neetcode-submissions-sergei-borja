class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = defaultdict(int)

        for i in nums:
            freq_dict[i] += 1

        res = sorted(freq_dict, key=freq_dict.get, reverse=True)

        return res[:k]
