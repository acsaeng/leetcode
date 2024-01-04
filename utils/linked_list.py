# Definition for singly-linked list
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


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
