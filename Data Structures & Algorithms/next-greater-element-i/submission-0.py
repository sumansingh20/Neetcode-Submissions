class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        greater = {}
        for x in nums2:
            while stack and x > stack[-1]:
                greater[stack.pop()] = x
            stack.append(x)
        for x in stack:
            greater[x] = -1
        return [greater[x] for x in nums1]