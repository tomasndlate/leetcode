class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalindrome(left, right):
            while left <= right and s[left] == s[right]:
                left += 1
                right -=1
            return right < left 

        res = []

        def dp(start, path):
            if start == len(s):
                res.append(path[:])

            for i in range(start, len(s)):
                if isPalindrome(start, i):
                    path.append(s[start:i+1])
                    dp(i+1, path)
                    path.pop()

        dp(0, [])
        return res
        
