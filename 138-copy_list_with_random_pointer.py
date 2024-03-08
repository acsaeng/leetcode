from typing import Optional

class Node:
  def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
    self.val = int(x)
    self.next = next
    self.random = random


class Solution:
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    node_map = { None: None }
    cursor = head

    while cursor:
      copy = Node(cursor.val)
      node_map[cursor] = copy
      cursor = cursor.next
    
    cursor = head

    while cursor:
      copy = node_map[cursor]
      copy.next = node_map[cursor.next]
      copy.random = node_map[cursor.random]
      cursor = cursor.next

    return node_map[head]