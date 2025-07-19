class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # min length array in A, and max length array on B (guarantee safe boundaries)
        # find what index is median
        # partition A in half, and complete total left partition with elements of B
        # if partition is valid (all elements are part of left) return median
        # else, move A left partition to left or right, depending on condition
        # loop again
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        total = len(A) + len(B)
        half = total // 2

        leftA, rightA = 0, len(A)
        while leftA <= rightA:
            partitionA = (leftA + rightA) // 2
            partitionB = half - partitionA

            Aleft = A[partitionA - 1] if partitionA > 0 else float('-inf')
            Bleft = B[partitionB - 1] if partitionB > 0 else float('-inf')

            Aright = A[partitionA] if partitionA < len(A) else float('inf')
            Bright = B[partitionB] if partitionB < len(B) else float('inf')

            # if partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # not correct partition
            if Aleft <= Bright: # bigger Aleft
                leftA = partitionA + 1
            else:
                rightA = partitionA - 1

        return 0.0
