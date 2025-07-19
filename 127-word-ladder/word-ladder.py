from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        letters = defaultdict(set) # index: [possible letters]
        for word in wordList:
            for i, letter in enumerate(word):
                letters[i].add(letter)

        seen = set() # word: numTransform
        words = set(wordList)
        words.add(beginWord)

        if endWord not in words:
            return 0

        queue = deque([ (beginWord, 1) ])
        
        while queue:
            word, numTransform = queue.popleft()

            # Already search these word or Not a word
            if word in seen or word not in words:
                continue
            
            seen.add(word)

            # Found same word
            if word == endWord:
                return numTransform
            
            wordArray = list(word)
            for i, curLetter in enumerate(word):
                for newLetter in letters[i]:
                    if curLetter != newLetter:
                        wordArray[i] = newLetter
                        queue.append(("".join(wordArray), numTransform + 1))
                        wordArray[i] = curLetter

        #dfs(list(beginWord), 1)
        return 0
