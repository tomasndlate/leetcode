class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        i, j = 0, n-1

        while i < j:
            while numbers[i] + numbers[j] < target: i += 1
            while numbers[i] + numbers[j] > target: j -= 1
            if numbers[i] + numbers[j] == target: return [i+1, j+1]
        
        return [-1, -1]
