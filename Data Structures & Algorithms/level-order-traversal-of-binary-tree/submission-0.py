# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def levelOrderRec(root, level, res):
            if root is None:
                return
            
            if len(res) <= level:
                res.append([])

            res[level].append(root.val)

            levelOrderRec(root.left, level+1, res)
            levelOrderRec(root.right, level+1, res)

        res = []
        levelOrderRec(root, 0, res)
        return res