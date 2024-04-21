class Node:
  def __init__(self, key=0, val=0, prev=None, next=None):
    self.key = key
    self.val = val
    self.prev = prev
    self.next = next


class LRUCache:
  def __init__(self, capacity: int):
    self.capacity = capacity
    self.cache = {}

    # left is least recently used, right is most recently used
    self.left, self.right = Node(), Node()
    self.left.next, self.right.prev = self.right, self.left

  def get(self, key: int) -> int:
    if key in self.cache:
      self.remove(self.cache[key])
      self.insert(self.cache[key])
      return self.cache[key].val
    else:
      return -1

  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      self.remove(self.cache[key])

    self.cache[key] = Node(key, value)
    self.insert(self.cache[key])

    if len(self.cache) > self.capacity:
      lru = self.left.next
      self.remove(lru)
      del self.cache[lru.key]
  
  def insert(self, node):
    prev, next = self.right.prev, self.right
    prev.next = next.prev = node
    node.prev, node.next = prev, next

  def remove(self, node):
    prev, next = node.prev, node.next
    prev.next, next.prev = next, prev


print('Case 1: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"], [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]')
lRUCache  = LRUCache(2)
print([None, lRUCache.put(1, 1), lRUCache.put(2, 2), lRUCache.get(1), lRUCache.put(3, 3), lRUCache.get(2), lRUCache.put(4, 4), lRUCache.get(1), lRUCache.get(3), lRUCache.get(4)])