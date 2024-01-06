from typing import Optional
from utils.binary_tree import binary_tree_to_list, list_to_binary_tree, TreeNode

class Solution:
  def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
      return
    else:
      root.left, root.right = root.right, root.left
      self.invertTree(root.left)
      self.invertTree(root.right)
    
    return root


print('Case 1: head = [4, 2, 7, 1, 3, 6, 9]')
ans = Solution().invertTree(list_to_binary_tree([4, 2, 7, 1, 3, 6, 9]))
print('Answer:', binary_tree_to_list(ans))

print('\nCase 2: head = [2, 1, 3]')
ans = Solution().invertTree(list_to_binary_tree([2, 1, 3]))
print('Answer:', binary_tree_to_list(ans))

print('\nCase 3: head = []')
ans = Solution().invertTree(list_to_binary_tree([]))
print('Answer:', binary_tree_to_list(ans))