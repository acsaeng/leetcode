from typing import Optional
from utils.linked_list import ListNode, linked_list_to_list, list_to_linked_list

class Solution:
  def reorderList(self, head: Optional[ListNode]) -> None:
    slow = head
    fast = head.next

    # Find middle of linked list
    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next

    # Reverse pointers in second half of linked list
    cursor = slow.next
    prev_cursor = slow.next = None
    
    while cursor:
      next_cursor = cursor.next
      cursor.next = prev_cursor
      prev_cursor = cursor
      cursor = next_cursor
    
    # Merge the two halved linked lists
    tail = prev_cursor

    while tail:
      next_head, next_tail = head.next, tail.next
      head.next = tail
      tail.next = next_head
      head, tail = next_head, next_tail


print('Case 1: head = [1, 2, 3, 4]')
head = list_to_linked_list([1, 2, 3, 4])
Solution().reorderList(head)
print('Answer:', linked_list_to_list(head))

print('\nCase 2: head = [1, 2, 3, 4, 5]')
head = list_to_linked_list([1, 2, 3, 4, 5])
Solution().reorderList(head)
print('Answer:', linked_list_to_list(head))

        