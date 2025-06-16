class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefixSum = [0] * (n + 1)
        for i in range(n):
            self.prefixSum[i+1] = self.prefixSum[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum[right+1] - self.prefixSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)