# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        res = []
        curr = []

        def generatePath(node, remain):
            if node == None:
                return
            
            remain -= node.val
            curr.append(node.val)
            
            if node.right == None and node.left == None:
                if remain == 0:
                    res.append(curr[:])

            if node.left: generatePath(node.left, remain)
            if node.right: generatePath(node.right, remain)
            curr.pop()
            
        if root is None and targetSum == 0:
            return []

        generatePath(root, targetSum)
        return res