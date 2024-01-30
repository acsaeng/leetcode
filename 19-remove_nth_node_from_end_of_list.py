from typing import Optional
from utils.linked_list import linked_list_to_list, list_to_linked_list, ListNode

class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    if not head.next:
      return None

    nth = end = head

    while end.next:
      end = end.next

      if n > 0:
        n -= 1
      else:
        nth = nth.next
    
    if n:
      head = head.next
    else:
      nth.next = nth.next.next

    return head


print('Case 1: head = [1, 2, 3, 4, 5], , n = 2')
ans = Solution().removeNthFromEnd(list_to_linked_list([1, 2, 3, 4, 5]), 2)
print('Answer:', linked_list_to_list(ans))

print('\nCase 2: head = [1], 1')
ans = Solution().removeNthFromEnd(list_to_linked_list([1]), 1)
print('Answer:', linked_list_to_list(ans))

print('\nCase 3: head = [1, 2], n = 1')
ans = Solution().removeNthFromEnd(list_to_linked_list([1, 2]), 1)
print('Answer:', linked_list_to_list(ans))