from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        words = set(wordList)

        if endWord not in words:
            return 0

        letters = defaultdict(set)
        for word in words:
            for i, c in enumerate(word):
                letters[i].add(c)

        queue = deque([beginWord])
        visited = set([beginWord])
        transformations = 1
        while queue:
            length = len(queue)

            for _ in range(length):
                word = queue.popleft()

                if word == endWord:
                    return transformations

                editWord = list(word)
                for i in range(len(word)):
                    temp = editWord[i]
                    for c in letters[i]:
                        editWord[i] = c
                        newWord = "".join(editWord)
                        if newWord in words and newWord not in visited:
                            visited.add(newWord)
                            queue.append(newWord)
                    editWord[i] = temp

            transformations += 1
        
        return 0
