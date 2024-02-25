from typing import Optional
from utils.binary_tree import list_to_binary_tree, TreeNode

class Solution:
  def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
    level_ordered_nodes = []
    queue = [root]
    
    while queue:
      num_nodes_in_level = len(queue)
      level = []

      for _ in range(num_nodes_in_level):
        node = queue.pop(0)

        if node:
          level.append(node.val)
          queue.append(node.left)
          queue.append(node.right)
      
      if level: level_ordered_nodes.append(level)
    
    return level_ordered_nodes


print('Case 1: root = [3, 9, 20, null, null, 15, 7]')
print('Answer:', Solution().levelOrder(list_to_binary_tree([3, 9, 20, None, None, 15, 7])))
                                       
print('\nCase 2: root = [1]')
print('Answer:', Solution().levelOrder(list_to_binary_tree([1])))

print('\nCase 3: root = []')
print('Answer:', Solution().levelOrder(list_to_binary_tree([])))

