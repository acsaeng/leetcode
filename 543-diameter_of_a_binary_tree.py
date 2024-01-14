from typing import Optional
from utils.binary_tree import list_to_binary_tree, TreeNode

class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    def dfs(root):
      nonlocal max_diameter
      
      if not root:
        return 0
      else:
        left_len = dfs(root.left)
        right_len = dfs(root.right)
        max_diameter = max(max_diameter, left_len + right_len)

        return max(left_len, right_len) + 1
    
    max_diameter = 0
    dfs(root)
    return max_diameter


print('Case 1: root = [1, 2, 3, 4, 5]')
print('Answer:', Solution().diameterOfBinaryTree(list_to_binary_tree([1, 2, 3, 4, 5])))

print('\nCase 2: root = [1, 2]')
print('Answer:', Solution().diameterOfBinaryTree(list_to_binary_tree([1, 2])))