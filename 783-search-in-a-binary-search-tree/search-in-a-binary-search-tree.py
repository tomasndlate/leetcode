# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # RECURSION
        #if not root:
            #return None
        
        #if val < root.val:
        #    return self.searchBST(root.left, val)
        #elif val > root.val:
        #    return self.searchBST(root.right, val)
        #else:
        #    return root

        # ITERACTIVE
        while root:
            if val < root.val:
                root = root.left
            elif val > root.val:
                root = root.right
            else:
                return root
        return None
        
        