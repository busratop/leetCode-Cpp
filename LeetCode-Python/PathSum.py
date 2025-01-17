# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        # Eğer yaprak düğüme ulaştıysak, yolu kontrol et
        if not root.left and not root.right:
            return targetSum == root.val

        # Sol ve sağ alt ağaçları kontrol et
        targetSum -= root.val
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
