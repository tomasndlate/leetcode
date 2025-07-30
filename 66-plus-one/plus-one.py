class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = (digits[-1] + 1) // 10
        digits[-1] = (digits[-1] + 1) % 10
        
        for i in range(len(digits) - 2, -1, -1):
            if not carry:
                break
            num = digits[i] + carry
            carry = num // 10
            digits[i] = num % 10

        if carry:
            return [carry] + digits
        else:
            return digits