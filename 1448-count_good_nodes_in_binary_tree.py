from utils.binary_tree import TreeNode, list_to_binary_tree

class Solution:
  def __init__(self):
    self.num_good_nodes = 0

  def goodNodes(self, root: TreeNode) -> int:
    self.dfs(root, float('-inf'))
    return self.num_good_nodes
  
  def dfs(self, node, max_val):
    if not node:
      return
    else:
      if node.val >= max_val:
        self.num_good_nodes += 1
      
      self.dfs(node.left, max(node.val, max_val))
      self.dfs(node.right, max(node.val, max_val))


print('Case 1: root = [3, 1, 4, 3, null, 1, 5]')
print('Answer:', Solution().goodNodes(list_to_binary_tree([3, 1, 4, 3, None, 1, 5])))

print('\nCase 2: root = [3, 3, null, 4, 2]')
print('Answer:', Solution().goodNodes(list_to_binary_tree([3, 3, None, 4, 2])))

print('\nCase 2: root = [1]')
print('Answer:', Solution().goodNodes(list_to_binary_tree([1])))