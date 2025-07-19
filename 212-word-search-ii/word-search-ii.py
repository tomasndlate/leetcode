from collections import defaultdict
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordsDict = defaultdict(set) # index: set(words partitions until index)
        wordsSet = set(words)

        for word in words: # O(n)
            for i in range(len(word)): # O(1), max word length is 10
                wordsDict[i].add(word[:i+1])
        
        rows, cols = len(board), len(board[0])
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        seen = set() # (row, col)
        res = set()

        def dfs(row, col, path, i):
            path.append(board[row][col])
            word = "".join(path)
            
            if word not in wordsDict[i]:
                path.pop()
                return

            if word in wordsSet:
                res.add(word)
            
            seen.add((row, col))
            
            for x, y in directions:
                r = row + x
                c = col + y
                if (    0 <= r < rows 
                    and 0 <= c < cols
                    and (r, c) not in seen): # within bounds
                    dfs(r, c, path, i + 1)

            path.pop()
            seen.remove((row, col))
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, [], 0)
        
        return list(res)

