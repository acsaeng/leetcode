from typing import Optional
from utils.linked_list import linked_list_to_list, list_to_linked_list, ListNode

class Solution:
  def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head

    while fast and fast.next:
      slow = slow.next
      fast = fast.next.next
    
    return slow


print('Case 1: head = [1, 2, 3, 4, 5]')
ans = Solution().middleNode(list_to_linked_list([1, 2, 3, 4, 5]))
print('Answer:', linked_list_to_list(ans))

print('\nCase 2: head = [1, 2, 3, 4, 5, 6]')
ans = Solution().middleNode(list_to_linked_list([1, 2, 3, 4, 5, 6]))
print('Answer:', linked_list_to_list(ans))