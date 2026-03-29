class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Idx = { v:i for i,v in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []
        for i in nums2:
            while stack and i > stack[-1]:
                val = stack.pop()
                if val in nums1Idx:
                    res[nums1Idx[val]] = i
            stack.append(i)

        return res