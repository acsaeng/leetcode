# Definition for singly-linked list
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next


def list_to_linked_list(array):
  if not array:
    return None
  
  dummy = current = ListNode()

  for num in array:
    current.next = ListNode(num)
    current = current.next

  return dummy.next


def linked_list_to_list(head):
  linked_list_vals = []

  while head:
    linked_list_vals.append(head.val)
    head = head.next

  return linked_list_vals


def list_to_cycled_linked_list(array, pos):
  if not array:
    return None
  
  dummy = current = ListNode()
  cycled_node = None

  for i in range(len(array)):
    current.next = ListNode(array[i])
    current = current.next

    if i == pos:
      cycled_node = current
  
  current.next = cycled_node
  return dummy.next