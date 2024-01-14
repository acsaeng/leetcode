from typing import Optional
from utils.binary_tree import list_to_binary_tree, TreeNode

class Solution:
  def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
    return self.calculate_diameter(root)[1]
  
  def calculate_diameter(self, root):
    if not root:
      return [0, 0]
    else:
      left = self.calculate_diameter(root.left)
      right = self.calculate_diameter(root.right)

      return [max(left[0], right[0]) + 1, max(left[0] + right[0], left[1], right[1])]


print('Case 1: root = [1, 2, 3, 4, 5]')
print('Answer:', Solution().diameterOfBinaryTree(list_to_binary_tree([1, 2, 3, 4, 5])))

print('\nCase 2: root = [1, 2]')
print('Answer:', Solution().diameterOfBinaryTree(list_to_binary_tree([1, 2])))