# Definition for a binary tree node
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def list_to_binary_tree(array):
  if not array:
    return None

  root = TreeNode(array.pop(0))
  queue = [root]

  while array and queue:
    current_node = queue.pop(0)

    if array:
      left = array.pop(0)

      if left:
        current_node.left = TreeNode(left)
        queue.append(current_node.left)

    if array:
      right = array.pop(0)

      if right:
        current_node.right = TreeNode(right)
        queue.append(current_node.right)

  return root


def binary_tree_to_list(root):
  if not root:
    return []

  binary_tree_list = []
  queue = [root]
 
  while queue:
    node = queue.pop(0)
    binary_tree_list.append(node.val if node else None)

    if node:
      queue.append(node.left)
      queue.append(node.right)
  
  while not binary_tree_list[-1]:
    binary_tree_list.pop()

  return binary_tree_list


def get_node_from_value(root, value):
  if not root:
    return
  elif root.val == value:
    return root
  else:
    return get_node_from_value(root.left, value) or get_node_from_value(root.right, value)

