from typing import Optional
from utils.linked_list import ListNode, create_linked_list, print_linked_list

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
ans = solution.reverseList(create_linked_list([1, 2, 3, 4, 5]))
print('Answer:', print_linked_list(ans))

print('\nCase 2: head = [1, 2]')
ans = solution.reverseList(create_linked_list([1, 2]))
print('Answer:', print_linked_list(ans))

print('\nCase 3: head = []')
ans = solution.reverseList(create_linked_list([]))
print('Answer:', print_linked_list(ans))