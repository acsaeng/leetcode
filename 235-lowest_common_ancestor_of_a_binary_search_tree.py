from utils.binary_tree import binary_tree_to_list, get_node_from_value, list_to_binary_tree, TreeNode

class Solution:
  def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root:
      return
    elif root.val > p.val and root.val > q.val:
      return self.lowestCommonAncestor(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
      return self.lowestCommonAncestor(root.right, p, q)
    else:
      return root

print('Case 1: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 8')
tree = list_to_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
ans = Solution().lowestCommonAncestor(tree, get_node_from_value(tree, 2), get_node_from_value(tree, 8))
print('Answer:', ans.val)

print('\nCase 2: root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4')
tree = list_to_binary_tree([6, 2, 8, 0, 4, 7, 9, None, None, 3, 5])
ans = Solution().lowestCommonAncestor(tree, get_node_from_value(tree, 2), get_node_from_value(tree, 4))
print('Answer:', ans.val)

print('\nCase 3: root = [2, 1], p = 2, q = 1')
tree = list_to_binary_tree([2, 1])
ans = Solution().lowestCommonAncestor(tree, get_node_from_value(tree, 2), get_node_from_value(tree, 1))
print('Answer:', ans.val)