from typing import Optional
from utils.binary_tree import TreeNode, list_to_binary_tree

class Solution:
  def isValidBST(self, root: Optional[TreeNode]) -> bool:
    return self.dfs(root, [float('-inf'), float('inf')])
  
  def dfs(self, node, val_range):
    if not node:
      return True
    elif (node.left and node.left.val >= node.val) or (node.right and node.right.val <= node.val) or not (val_range[0] < node.val < val_range[1]):
      return False
    else:
      return self.dfs(node.left, [min(node.val, val_range[0]), min(node.val, val_range[1])]) and self.dfs(node.right, [max(node.val, val_range[0]), max(node.val, val_range[1])])
  

print('Case 1: root = [2, 1, 3]')
print('Answer:', Solution().isValidBST(list_to_binary_tree([2, 1, 3])))
                                       
print('\nCase 2: root = [5, 1, 4, null, null, 3, 6]')
print('Answer:', Solution().isValidBST(list_to_binary_tree([5, 1, 4, None, None, 3, 6])))