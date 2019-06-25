class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def invertTree(root: TreeNode) -> TreeNode:
    if root is None:
        return None

    root.left, root.right = invertTree(root.right), invertTree(root.left)
    return root


def printThreeDepthTree(root: TreeNode) -> None:
    print(root.val)
    print(root.left.val, root.right.val)
    print(root.left.left.val, root.left.right.val,
          root.right.left.val, root.right.right.val)


tree = TreeNode(4)
tree.left = TreeNode(2)
tree.right = TreeNode(7)
tree.left.left = TreeNode(1)
tree.left.right = TreeNode(3)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(9)

printThreeDepthTree(tree)
solution = invertTree(tree)
printThreeDepthTree(solution)
