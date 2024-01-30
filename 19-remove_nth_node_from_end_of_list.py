from typing import Optional
from utils.linked_list import linked_list_to_list, list_to_linked_list, ListNode

class Solution:
  def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = left = ListNode(None, head)
    right = head

    while n > 0 and right:
      right = right.next
      n -= 1
    
    while right:
      left = left.next
      right = right.next
    
    left.next = left.next.next
    return dummy.next


print('Case 1: head = [1, 2, 3, 4, 5], , n = 2')
ans = Solution().removeNthFromEnd(list_to_linked_list([1, 2, 3, 4, 5]), 2)
print('Answer:', linked_list_to_list(ans))

print('\nCase 2: head = [1], 1')
ans = Solution().removeNthFromEnd(list_to_linked_list([1]), 1)
print('Answer:', linked_list_to_list(ans))

print('\nCase 3: head = [1, 2], n = 1')
ans = Solution().removeNthFromEnd(list_to_linked_list([1, 2]), 1)
print('Answer:', linked_list_to_list(ans))