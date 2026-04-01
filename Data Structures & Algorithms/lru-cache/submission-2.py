class Node:

    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.l, self.r = Node(0, 0), Node(0, 0)
        self.l.next = self.r
        self.r.prev = self.l

    def insert(self, node):
        prev, next = self.r.prev, self.r
        prev.next = next.prev = node
        node.prev, node.next = prev, next

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            self.cache[key].val = value
            self.remove(self.cache[key])
            self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.l.next
            del self.cache[lru.key]
            self.remove(lru)

























# class Node:

#     def __init__(self, key, val):
#         self.key = key
#         self.val = val
#         self.prev = self.nxt = None

# class LRUCache:

#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}
#         self.left, self.right = Node(0, 0), Node(0, 0)
#         self.left.nxt = self.right
#         self.right.prev = self.left

#     def insert(self, node):
#         prev, nxt = self.right.prev, self.right
#         node.prev = prev
#         node.nxt = nxt
#         prev.nxt = nxt.prev = node

#     def remove(self, node):
#         prev = node.prev
#         nxt = node.nxt
#         prev.nxt = nxt
#         nxt.prev = prev
        
#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])
#         if len(self.cache) > self.cap:
#             lru = self.left.nxt
#             self.remove(lru)
#             del self.cache[lru.key]
