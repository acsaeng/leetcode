from typing import Optional
from utils.binary_tree import binary_tree_to_list, list_to_binary_tree, TreeNode

class Solution:
  def isBalanced(self, root: Optional[TreeNode]) -> bool:
    return self.check_balanced_tree(root)[0]
  
  def check_balanced_tree(self, root):
    if not root: 
      return [True, 0]
    elif not root.left and not root.right:
      return [True, 1]
    elif not root.left:
      right = self.check_balanced_tree(root.right)
      return [right[0] and right[1] <= 1, right[1] + 1]
    elif not root.right:
      left = self.check_balanced_tree(root.left)
      return [left[0] and left[1] <= 1, left[1] + 1]
    else:
      left = self.check_balanced_tree(root.left)
      right = self.check_balanced_tree(root.right)
      return [left[0] and right[0] and abs(left[1] - right[1]) <= 1, max(left[1], right[1]) + 1]
  

print('Case 1: root = [3, 9, 20, null, null, 15, 7]')
print('Answer:', Solution().isBalanced(list_to_binary_tree([3, 9, 20, None, None, 15, 7])))
                                       
print('\nCase 2: root = [1, 2, 2, 3, 3, null, null, 4, 4]')
print('Answer:', Solution().isBalanced(list_to_binary_tree([1, 2, 2, 3, 3, None, None, 4, 4])))

print('\nCase 3: root = []')
print('Answer:', Solution().isBalanced(list_to_binary_tree([])))

print('\nCase: root = [1, 2, 2, 3, null, null, 3, 4, null, null, 4]')
print('Answer:', Solution().isBalanced(list_to_binary_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4])))