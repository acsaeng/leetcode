from typing import Optional
from utils.binary_tree import TreeNode, list_to_binary_tree

class Solution:
  def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    stack = []
    node = root

    while node or stack:
      while node:
        stack.append(node)
        node = node.left
      
      node = stack.pop()
      k -= 1

      if k == 0:
        return node.val

      node = node.right


print('Case 1: root = [3, 1, 4, null, 2], k = 1')
print(Solution().kthSmallest(list_to_binary_tree([3, 1, 4, None, 2]), 1))

print('\nCase 2: root = [5, 3, 6, 2, 4, null, null, 1], k = 3')
print(Solution().kthSmallest(list_to_binary_tree([5, 3, 6, 2, 4, None, None, 1]), 3))