from typing import Optional

# Definition for singly-linked list
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


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


def create_linked_list(array):
  if array:
    cursor = first_node = ListNode(array[0], next=None)

    for i in range(1, len(array)):
      cursor.next = ListNode(array[i], next=cursor if i != len(array) - 1 else None)
      cursor = cursor.next

    return first_node


def print_linked_list(head):
  cursor = head
  linked_list_vals = []

  while cursor:
    linked_list_vals.append(cursor.val)
    cursor = cursor.next

  return linked_list_vals


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