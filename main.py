class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self, root):
        self.root = Tree(root)

    def search(self, root, target):
        if root is None:
            return False
        elif target > root.val:
            return self.search(root.right, target)
        elif target < root.val:
            return self.search(root.left, target)
        else:
            return True

    def insertion(self, root, val):
        if root is None:
            return Tree(val)
        if val > root.val:
            root.right = self.insertion(root.right, val)
        elif val < root.val:
            root.left = self.insertion(root.left, val)
        return root

    def minNode_val(self, root):
        cur = root
        while cur and cur.left:
            cur = cur.left
        return cur.val

    def remove(self, root, val):
        if root is None: # if we reach the end and can't find the node that needed to be deleted
            return False
        if val > root.val:
            root.right = self.remove(root.right, val) # recursive calls that allows us to progress along the tree
        elif val < root.val:
            root.left = self.remove(root.left, val)
        else: # case where we find the node with the val we want to delete
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                min_node_val = self.minNode(root.right)
                root.val = min_node_val
                root.right = self.remove(root.right, min_node_val)


    def inorder(self, root):
        # left_child -> parent -> right_child
        if root is None:
            return
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

    def inorder_array(self, root, array):
        if root is None:
            return
        self.inorder_array(root.left, array)
        array.append(root.val)
        self.inorder_array(root.right, array)

    def sort_array(self, nums):
        # if a given array is empty we can just return an empty list
        if not nums:
            return nums
        root = None
        for num in nums:
            root = self.insertion(root, num)
        sorted_array = []
        self.inorder_array(root, sorted_array)
        return sorted_array



    def preorder(self, root):
        # parent -> left_child -> right_child
        if root is None:
            return
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)



    def postorder(self, root):
        # left_child -> right_child -> parent
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)





tree = BinaryTree(4)
tree.insertion(tree.root, 3)
tree.insertion(tree.root, 6)
tree.insertion(tree.root, 5)
tree.insertion(tree.root, 7)
tree.insertion(tree.root, 2)
tree.search(tree.root, 7)


