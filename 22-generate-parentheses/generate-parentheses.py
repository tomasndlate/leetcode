class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def backtrack(opening, closing, path):

            if opening <= n: # add open
                path.append("(")
                backtrack(opening + 1, closing, path)
                path.pop()

            if closing < opening: # add close
                path.append(")")
                backtrack(opening, closing + 1, path)
                path.pop()

            if opening == closing == n: # append
                res.append("".join(path))
        
        backtrack(0, 0, [])
        return res