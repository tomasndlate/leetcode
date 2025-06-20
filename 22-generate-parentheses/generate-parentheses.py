class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, opening, closing):
            if opening < n:
                path.append("(")
                backtrack(path, opening + 1, closing)
                path.pop()

            if closing < opening:
                path.append(")")
                backtrack(path, opening, closing + 1)
                path.pop()
            
            if closing == n:
                res.append("".join(path))

        backtrack([], 0, 0)
        return res