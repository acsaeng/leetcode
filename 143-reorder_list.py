from typing import Optional
from utils.linked_list import ListNode, linked_list_to_list, list_to_linked_list

class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    tail = head

    while tail.next:
      tail = tail.next
    
    while head != tail:
      head.next, tail.next = tail, head.next
      head = tail.next

      while tail.next.next != head:
        tail = tail.next
    
    head.next = None
    

print('Case 1: head = [1, 2, 3, 4]')
head = list_to_linked_list([1, 2, 3, 4])
Solution().reorderList(head)
print('Answer:', linked_list_to_list(head))

print('\nCase 2: head = [1, 2, 3, 4, 5]')
head = list_to_linked_list([1, 2, 3, 4, 5])
Solution().reorderList(head)
print('Answer:', linked_list_to_list(head))

        