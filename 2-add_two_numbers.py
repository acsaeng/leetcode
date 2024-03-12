from typing import Optional
from utils.linked_list import linked_list_to_list, list_to_linked_list, ListNode

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    cursor1, cursor2 = l1, l2
    result = result_cursor = ListNode()
    carry = 0

    while cursor1 or cursor2:
      operand1 = cursor1.val if cursor1 else 0
      operand2 = cursor2.val if cursor2 else 0
      sum = operand1 + operand2 + carry

      if sum >= 10:
        sum -= 10
        carry = 1
      else:
        carry = 0

      result_cursor.next = ListNode(sum)

      if cursor1: cursor1 = cursor1.next
      if cursor2: cursor2 = cursor2.next
      result_cursor = result_cursor.next
    
    if carry: 
      result_cursor.next = ListNode(carry)

    return result.next


print('Case 1: l1 = [2, 4, 3], l2 = [5, 6, 4]')
ans = Solution().addTwoNumbers(list_to_linked_list([2, 4, 3]), list_to_linked_list([5, 6, 4]))
print('Answer:', linked_list_to_list(ans))

print('\nCase 2: l1 = [0], l2 = [0]')
ans = Solution().addTwoNumbers(list_to_linked_list([0]), list_to_linked_list([0]))
print('Answer:', linked_list_to_list(ans))

print('\nCase 3: l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]')
ans = Solution().addTwoNumbers(list_to_linked_list([9, 9, 9, 9, 9, 9, 9]), list_to_linked_list([9, 9, 9, 9]))
print('Answer:', linked_list_to_list(ans))