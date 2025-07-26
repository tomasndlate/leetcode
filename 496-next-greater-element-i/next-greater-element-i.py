class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2Map = { num: i for i, num in enumerate(nums2) }
        nextGreater = [-1] * len(nums2)
        stack = []

        for num in reversed(nums2):
            while stack and stack[-1] <= num:
                stack.pop()
            if stack:
                nextGreater[nums2Map[num]] = stack[-1]
            stack.append(num)

        res = [-1] * len(nums1)
        for i, num in enumerate(nums1):
            res[i] = nextGreater[nums2Map[num]]
        
        return res
