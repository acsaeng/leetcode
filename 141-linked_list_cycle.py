from typing import Optional
from utils.linked_list import list_to_cycled_linked_list, ListNode

class Solution:
  def hasCycle(self, head: Optional[ListNode]) -> bool:    
    tortoise = hare = head

    while hare and hare.next:
      tortoise = tortoise.next
      hare = hare.next.next
    
      if tortoise == hare:
        return True
    
    return False


print('Case 1: head = [3, 2, 0, -4], pos = 1')
print('Answer:', Solution().hasCycle(list_to_cycled_linked_list([3, 2, 0, -4], 1)))

print('\nCase 2: head = [1, 2], pos = 0')
print('Answer:', Solution().hasCycle(list_to_cycled_linked_list([1, 2], 0)))

print('\nCase 3: head = [1], pos = -1')
print('Answer:', Solution().hasCycle(list_to_cycled_linked_list([1], -1)))