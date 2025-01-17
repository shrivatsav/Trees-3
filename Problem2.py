# // Time Complexity : O(n) where n is the number of nodes in the graph.
# // Space Complexity : O(h) where h is the height of the tree.
# // Did this code successfully run on Leetcode : Yes
# // Any problem you faced while coding this : Class Solution.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        def helper(left,right):
            if left == None and right == None:
                return True
            if left == None or right == None:
                return False
            if left.val != right.val:
                return False
            
            return helper(left.left,right.right) and helper(left.right, right.left)
            
        return helper(root.left,root.right)
