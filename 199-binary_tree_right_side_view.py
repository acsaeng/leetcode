from typing import Optional
from utils.binary_tree import list_to_binary_tree, TreeNode

class Solution:
  def rightSideView(self, root: Optional[TreeNode]) -> list[int]:
    right_side_vals = []
    queue = [root] if root else []

    while queue:
      right_side_vals.append(queue[-1].val)

      for _ in range(len(queue)):
        node = queue.pop(0)
        if node.left: queue.append(node.left)
        if node.right: queue.append(node.right)
      
    return right_side_vals


print('Case 1: root = [1, 2, 3, null, 5, null, 4]')
print(Solution().rightSideView(list_to_binary_tree([1, 2, 3, None, 5, None, 4])))

print('\nCase 2: root = [1, null, 3]')
print(Solution().rightSideView(list_to_binary_tree([1, None, 3])))

print('\nCase 3: root = []')
print(Solution().rightSideView(list_to_binary_tree([])))