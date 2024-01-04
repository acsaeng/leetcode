from typing import Optional
from utils.linked_list import ListNode, create_linked_list, print_linked_list

class Solution:
  def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy_list = current_node = ListNode()

    while list1 and list2:
      if list1.val <= list2.val:
        current_node.next = list1
        list1 = list1.next
      else:
        current_node.next = list2
        list2 = list2.next
      
      current_node = current_node.next
    
    if list1:
      current_node.next = list1
    elif list2:
      current_node.next = list2
      
    return dummy_list.next


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