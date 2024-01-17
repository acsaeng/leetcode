from typing import Optional
from utils.binary_tree import list_to_binary_tree, TreeNode

class Solution:
  def maxDepth(self, root: Optional[TreeNode]) -> int:
    if not root:
      return 0
    
    return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


print('Case 1: root = [3, 9, 20, null, null, 15, 7]')
print('Answer:', Solution().maxDepth(list_to_binary_tree([3, 9, 20, None, None, 15,  7])))
                                       
print('\nCase 2: root = [1, null, 2]')
print('Answer:', Solution().maxDepth(list_to_binary_tree([1, None, 2])))
