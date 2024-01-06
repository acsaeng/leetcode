from typing import Optional
from utils.linked_list import linked_list_to_list, list_to_linked_list, ListNode

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    previous_node = None
    current_node = head

    while current_node:
      next_node = current_node.next
      current_node.next = previous_node
      previous_node = current_node
      current_node = next_node

    return previous_node


solution = Solution()

print('Case 1: head = [1, 2, 3, 4, 5]')
ans = solution.reverseList(list_to_linked_list([1, 2, 3, 4, 5]))
print('Answer:', linked_list_to_list(ans))

print('\nCase 2: head = [1, 2]')
ans = solution.reverseList(list_to_linked_list([1, 2]))
print('Answer:', linked_list_to_list(ans))

print('\nCase 3: head = []')
ans = solution.reverseList(list_to_linked_list([]))
print('Answer:', linked_list_to_list(ans))