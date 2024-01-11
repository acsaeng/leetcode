from typing import Optional
from utils.linked_list import list_to_cycled_linked_list, ListNode

class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:
    nodes = []
    
    while head:
      if head in nodes and len(nodes) > 1:
        return True
      
      nodes.append(head)
      head = head.next
    
    return False


print('Case 1: head = [3, 2, 0, -4], pos = 1')
print('Answer:', Solution().hasCycle(list_to_cycled_linked_list([3, 2, 0, -4], 1)))

print('\nCase 2: head = [1, 2], pos = 0')
print('Answer:', Solution().hasCycle(list_to_cycled_linked_list([1, 2], 0)))

print('\nCase 3: head = [1], pos = -1')
print('Answer:', Solution().hasCycle(list_to_cycled_linked_list([1], -1)))