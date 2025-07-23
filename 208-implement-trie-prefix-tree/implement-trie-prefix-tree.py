class Trie:

    def __init__(self):
        self.head = Node()

    def insert(self, word: str) -> None:
        node = self.head
        for letter in word:
            if letter not in node.children:
                node.children[letter] = Node()
            node = node.children[letter]
        node.children["*"] = None # ending word


    def search(self, word: str) -> bool: # exact word
        node = self.head
        for letter in word:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return "*" in node.children # ending word ?
        

    def startsWith(self, prefix: str) -> bool:
        node = self.head
        for letter in prefix:
            if letter not in node.children:
                return False
            node = node.children[letter]
        return True
        
class Node:
    def __init__(self):
        self.children = {}

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)