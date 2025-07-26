class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.nodes = {} # key: Node
        self.head = None
        self.tail = None
        

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1

        node = self.nodes[key]
        self.moveToHead(node)

        return node.value
        

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.value = value
            self.moveToHead(node)
        else:
            newNode = Node(key, value)
            self.nodes[key] = newNode
            self.addToHead(newNode)
            if len(self.nodes) > self.capacity:
                self.removeTail()

    def addToHead(self, node):
        node.prev = None
        node.next = self.head

        if self.head:
            self.head.prev = node
        self.head = node

        if not self.tail:
            self.tail = node

    def moveToHead(self, node):
        if node == self.head:
            return

        # Disconnect node
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

        if node == self.tail:
            self.tail = node.prev

        # Re-add to head
        self.addToHead(node)

    def removeTail(self):
        if not self.tail:
            return
        
        key = self.tail.key
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else: # only 1 item
            self.head = self.tail = None

        del self.nodes[key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)