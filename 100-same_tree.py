from typing import Optional
from utils.binary_tree import list_to_binary_tree, TreeNode

class Solution:
  def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
      return True
    elif not p or not q or p.val != q.val:
      return False
    else:
      return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


print('Case 1: p = [1, 2, 3], q = [1, 2, 3]')
print('Answer:', Solution().isSameTree(list_to_binary_tree([1, 2, 3]), list_to_binary_tree([1, 2, 3])))
                                       
print('\nCase 2: p = [1, 2], q = [1, null, 2]')
print('Answer:', Solution().isSameTree(list_to_binary_tree([1, 2]), list_to_binary_tree([1, None, 2])))

print('\nCase 3: p = [1, 2, 1], q = [1, 1, 2]')
print('Answer:', Solution().isSameTree(list_to_binary_tree([1, 2, 1]), list_to_binary_tree([1, 1, 2])))