class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.store = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.store:
            self.remove(self.store[key])
            self.insert(self.store[key])
            return self.store[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.store:
            self.remove(self.store[key])
        node = Node(key, value)
        self.store[key] = node
        self.insert(node)

        if len(self.store) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.store[lru.key]