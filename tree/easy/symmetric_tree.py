# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self.check_mirror(root.left, root.right)

    def check_mirror(
        self, left_node: Optional[TreeNode], right_node: Optional[TreeNode]
    ) -> bool:
        if left_node and right_node:
            return (
                left_node.val == right_node.val
                and self.check_mirror(left_node.left, right_node.right)
                and self.check_mirror(left_node.right, right_node.left)
            )
        return left_node == right_node
