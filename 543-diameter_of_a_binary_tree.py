from typing import Optional
from utils.binary_tree import list_to_binary_tree, TreeNode

class Solution:
  def __init__(self):
    self.max_diameter = 0

  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    self.dfs(root)
    return self.max_diameter

  def dfs(self, root):
    if not root:
      return 0
    else:
      left_len = self.dfs(root.left)
      right_len = self.dfs(root.right)
      self.max_diameter = max(self.max_diameter, left_len + right_len)

      return max(left_len, right_len) + 1


print('Case 1: root = [1, 2, 3, 4, 5]')
print('Answer:', Solution().diameterOfBinaryTree(list_to_binary_tree([1, 2, 3, 4, 5])))

print('\nCase 2: root = [1, 2]')
print('Answer:', Solution().diameterOfBinaryTree(list_to_binary_tree([1, 2])))