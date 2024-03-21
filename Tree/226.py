'''

we can get curr node  + left and right child

set left child of node to be right 
set right child of node to be left

and keep doing that recursively 



'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def recursion(root: Optional[TreeNode]):
    if root == None: return 

    left = root.left
    right = root.right

    root.right = left
    root.left = right

    recursion(left)
    recursion(right)

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    this.recursion(root)
    return root
    
