from collections import deque
class WordDictionary:

    def __init__(self):
        self.head = Node()

    def addWord(self, word: str) -> None:
        node = self.head
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.isWord = True

    def search(self, word: str) -> bool:

        def containWord(node, subWord):
            if not subWord:
                return node.isWord
            c = subWord[0]
            if c == ".":
                for child in node.children.values():
                    if containWord(child, subWord[1:]):
                        return True
                return False
            if c not in node.children:
                return False
            return containWord(node.children[c], subWord[1:])

        return containWord(self.head, word)


class Node:
    def __init__(self):
        self.children = {}
        self.isWord = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)