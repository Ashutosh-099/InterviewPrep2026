# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversal(self, node: TreeNode | None, curr: str, result: list[str]):
        if node == None:
            return

        curr += str(node.val)
        
        if node.left == None and node.right == None:
            # Leaf node
            result.append(curr)
            return

        curr += "->"
        self.traversal(node.left, curr, result)
        self.traversal(node.right, curr, result)
        return

    def binaryTreePaths(self, root: TreeNode | None) -> list[str]:
        result = []
        self.traversal(root, "", result)
        return result