from typing import Optional
from utils.binary_tree import list_to_binary_tree, TreeNode, binary_tree_to_list

class Solution:
  def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    if (root and not subRoot) or (not root and subRoot):
      return False
    elif self.same_tree(root, subRoot):
      return True
    
    return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
  
  def same_tree(self, root, subRoot):
    if not root and not subRoot:
      return True
    elif not root or not subRoot or root.val != subRoot.val:
      return False
    else:
      return self.same_tree(root.left, subRoot.left) and self.same_tree(root.right, subRoot.right)


print('Case 1: root = [3, 4, 5, 1, 2], subRoot = [4, 1, 2]')
print('Answer:', Solution().isSubtree(list_to_binary_tree([3, 4, 5, 1, 2]), list_to_binary_tree([4, 1, 2])))

print('\nCase 2: root = [3, 4, 5, 1, 2, null, null, null, null, 0], subRoot = [4, 1, 2]')
print('Answer:', Solution().isSubtree(list_to_binary_tree([3, 4, 5, 1, 2, None, None, None, None, 0]), list_to_binary_tree([4, 1, 2])))

