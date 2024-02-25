from typing import Optional
from utils.binary_tree import list_to_binary_tree, TreeNode

class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
    if not root:
      return []

    level_ordered_nodes = []
    parent_stack = [root]
    children_stack = []
    
    while parent_stack:
      level = []

      while parent_stack:
        node = parent_stack.pop(0)
        level.append(node.val)
    
        if node.left: children_stack.append(node.left)
        if node.right: children_stack.append(node.right)
      
      level_ordered_nodes.append(level)
      parent_stack = children_stack
      children_stack = []
    
    return level_ordered_nodes


print('Case 1: root = [3, 9, 20, null, null, 15, 7]')
print('Answer:', Solution().levelOrder(list_to_binary_tree([3, 9, 20, None, None, 15, 7])))
                                       
print('\nCase 2: root = [1]')
print('Answer:', Solution().levelOrder(list_to_binary_tree([1])))

print('\nCase 3: root = []')
print('Answer:', Solution().levelOrder(list_to_binary_tree([])))

