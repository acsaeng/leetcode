from typing import Optional
from utils.linked_list import linked_list_to_list, list_to_linked_list, ListNode

class Solution:
  def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    result = cursor = ListNode()
    carry = 0

    while l1 or l2:
      operand1 = l1.val if l1 else 0
      operand2 = l2.val if l2 else 0

      sum = operand1 + operand2 + carry
      carry = sum // 10
      sum %= 10
      
      cursor.next = ListNode(sum)

      if l1: l1 = l1.next
      if l2: l2 = l2.next
      cursor = cursor.next
    
    if carry: 
      cursor.next = ListNode(carry)

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