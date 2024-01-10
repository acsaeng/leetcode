from typing import Optional
from utils.binary_tree import list_to_binary_tree, TreeNode

class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    return self.check_balanced_tree(root)[0]
  
  def check_balanced_tree(self, root):
    if not root:
      return [True, 0]

    left = self.check_balanced_tree(root.left)
    right = self.check_balanced_tree(root.right)
    is_balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

    return [is_balanced, max(left[1], right[1]) + 1]
  

print('Case 1: root = [3, 9, 20, null, null, 15, 7]')
print('Answer:', Solution().isBalanced(list_to_binary_tree([3, 9, 20, None, None, 15, 7])))
                                       
print('\nCase 2: root = [1, 2, 2, 3, 3, null, null, 4, 4]')
print('Answer:', Solution().isBalanced(list_to_binary_tree([1, 2, 2, 3, 3, None, None, 4, 4])))

print('\nCase 3: root = []')
print('Answer:', Solution().isBalanced(list_to_binary_tree([])))