class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        letters = { "2": "abc", "3": "def", 
        "4": "ghi", "5": "jkl", "6": "mno", 
        "7": "pqrs", "8": "tuv", "9": "wxyz" }
        res = []

        def backtrack(start, path):
            if start == len(digits):
                res.append("".join(path))
                return
            
            for letter in letters[digits[start]]:
                path.append(letter)
                backtrack(start + 1, path)
                path.pop()
        
        backtrack(0, [])
        return res