from typing import Optional
from utils.binary_tree import TreeNode, list_to_binary_tree

class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    return self.dfs(root, [float('-inf'), float('inf')])
  
  def dfs(self, node, val_range):
    if not node:
      return True
    elif not (val_range[0] < node.val < val_range[1]):
      return False
    else:
      return self.dfs(node.left, [val_range[0], node.val]) and self.dfs(node.right, [node.val, val_range[1]])
  

print('Case 1: root = [2, 1, 3]')
print('Answer:', Solution().isValidBST(list_to_binary_tree([2, 1, 3])))
                                       
print('\nCase 2: root = [5, 1, 4, null, null, 3, 6]')
print('Answer:', Solution().isValidBST(list_to_binary_tree([5, 1, 4, None, None, 3, 6])))