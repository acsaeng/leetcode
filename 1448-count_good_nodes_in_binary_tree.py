from utils.binary_tree import TreeNode, list_to_binary_tree

class Solution:
  def goodNodes(self, root: TreeNode) -> int:
    return self.dfs(root, root.val)
  
  def dfs(self, node, max_val):
    if not node:
      return 0
    else:
      increment = 1 if node.val >= max_val else 0
      max_val = max(node.val, max_val)
      return self.dfs(node.left, max_val) + self.dfs(node.right, max_val) + increment


print('Case 1: root = [3, 1, 4, 3, null, 1, 5]')
print('Answer:', Solution().goodNodes(list_to_binary_tree([3, 1, 4, 3, None, 1, 5])))

print('\nCase 2: root = [3, 3, null, 4, 2]')
print('Answer:', Solution().goodNodes(list_to_binary_tree([3, 3, None, 4, 2])))

print('\nCase 2: root = [1]')
print('Answer:', Solution().goodNodes(list_to_binary_tree([1])))