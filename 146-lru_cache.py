class DoubleListNode:
  def __init__(self, key=0, val=0, prev=None, next=None):
    self.key = key
    self.val = val
    self.prev = prev
    self.next = next


class LRUCache:
  def __init__(self, capacity: int):
    self.cache = {}  # { key: int, value: DoubleListNode }
    self.capacity = capacity
    
    # left is least recently used (LRU), right is most recently used (MRU)
    self.lru_node, self.mru_node = DoubleListNode(), DoubleListNode()
    self.lru_node.next, self.mru_node.prev = self.mru_node, self.lru_node
    
  def get(self, key: int) -> int:
    if key in self.cache:
      value = self.cache[key].val
      self.delete_entry(key)
      self.insert_entry(key, value)
      return value
    else:
      return -1
        
  def put(self, key: int, value: int) -> None:
    if key in self.cache:
      self.delete_entry(key)
    elif len(self.cache) == self.capacity:
      self.delete_entry(self.lru_node.next.key)
    
    self.insert_entry(key, value)
    
  def insert_entry(self, key, value):
    new_node = DoubleListNode(key, value)
    self.cache[key] = new_node

    prev, next = self.mru_node.prev, self.mru_node
    new_node.prev, new_node.next = prev, next
    prev.next, next.prev = new_node, new_node

  def delete_entry(self, key):
    node = self.cache[key]
    prev, next = node.prev, node.next
    prev.next, next.prev = next, prev

    del self.cache[key]


print('Case 1: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"], [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]')
lRUCache  = LRUCache(2)
print([None, lRUCache.put(1, 1), lRUCache.put(2, 2), lRUCache.get(1), lRUCache.put(3, 3), lRUCache.get(2), lRUCache.put(4, 4), lRUCache.get(1), lRUCache.get(3), lRUCache.get(4)])