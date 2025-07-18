class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A = nums1
        B = nums2

        # make sure A contain smaller array
        if len(nums2) < len(nums1):
            A, B = B, A
        
        LENGTH = len(A) + len(B)
        HALF = LENGTH // 2

        # operate on A
        left, right = 0, len(A)
        while True:
            midA = (left + right) // 2
            midB = HALF - midA

            Aleft = A[midA - 1] if midA > 0 else float('-inf')
            Bleft = B[midB - 1] if midB > 0 else float('-inf')

            Aright = A[midA] if midA < len(A) else float('inf')
            Bright = B[midB] if midB < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright: # valid
                # odd
                if LENGTH % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            
            elif Aleft > Bright: # part A too big, need decrease
                right = midA - 1
            else: # part A too small, need increase
                left = midA + 1

