from typing import Optional
from utils.linked_list import ListNode, create_linked_list, print_linked_list

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if not list1 or not list2:
      return list1 or list2 or None
    
    if list1.val <= list2.val:
      head = current_node = list1
      other_node = list2
    else:
      head = current_node = list2
      other_node = list1

    while current_node.next or other_node:
      if not current_node.next:
        current_node.next = other_node
        break
      elif not other_node:
        break
      elif current_node.next.val > other_node.val:
        next_node = other_node
        other_node = current_node.next
        current_node.next = next_node
      
      current_node = current_node.next
      
    return head



  

solution = Solution()

print('Case 1: list1 = [1, 2, 4], list2 = [1, 3, 4]')
ans = solution.mergeTwoLists(create_linked_list([1, 2, 4]), (create_linked_list([1, 3, 4])))
print('Answer:', print_linked_list(ans))

print('\nCase 2: list1 = [], list2 = []')
ans = solution.mergeTwoLists(create_linked_list([]), create_linked_list([]))
print('Answer:', print_linked_list(ans))

print('\nCase 3: list1 = [], list2 = [0]')
ans = solution.mergeTwoLists(create_linked_list([]), create_linked_list([0]))
print('Answer:', print_linked_list(ans))