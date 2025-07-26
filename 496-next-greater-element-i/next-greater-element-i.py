class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = [-1] * len(nums2)

        for i in range(len(nums2) - 1, -1, -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                nextGreater[i] = stack[-1]
            stack.append(nums2[i])

        res = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            index = nums2.index(num)
            res[i] = nextGreater[index]
        
        return res
