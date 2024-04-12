from typing import Optional
from utils.binary_tree import TreeNode, binary_tree_to_list

class Solution:
  def buildTree(self, preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
      return None
    
    parent = TreeNode(preorder[0])
    partition_index = 0

    while inorder[partition_index] != preorder[0]:
      partition_index += 1
    
    parent.left = self.buildTree(preorder[1:partition_index + 1], inorder[0:partition_index])
    parent.right = self.buildTree(preorder[partition_index + 1:], inorder[partition_index + 1:])

    return parent


print('Case 1: preorder = [3, 9, 20, 15, 7], inorder = [9, 3, 15, 20, 7]')
print('Answer:', binary_tree_to_list(Solution().buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])))
                                       
print('\nCase 2: preorder = [-1], inorder = [-1]]')
print('Answer:', binary_tree_to_list(Solution().buildTree([-1], [-1])))