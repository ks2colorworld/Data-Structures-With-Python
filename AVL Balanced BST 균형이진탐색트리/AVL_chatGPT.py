class TreeNode:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.height(node.left), self.height(node.right))

    def balance_factor(self, node):
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self.update_height(y)
        self.update_height(x)

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self.update_height(x)
        self.update_height(y)

        return y

    def balance(self, node):
        if node is None:
            return None

        self.update_height(node)

        balance = self.balance_factor(node)

        # Left Heavy
        if balance > 1:
            # Left-Right Case
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Right Heavy
        if balance < -1:
            # Right-Left Case
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)

        if key < root.key:
            root.left = self.insert(root.left, key)
        elif key > root.key:
            root.right = self.insert(root.right, key)
        else:
            # Duplicate keys are not allowed
            return root

        return self.balance(root)

    def insert_key(self, key):
        self.root = self.insert(self.root, key)

    def inorder_traversal(self, root):
        result = []
        if root:
            result += self.inorder_traversal(root.left)
            result.append(root.key)
            result += self.inorder_traversal(root.right)
        return result

    def display_inorder(self):
        result = self.inorder_traversal(self.root)
        print("Inorder Traversal:", result)

# AVL Tree 예시
avl_tree = AVLTree()
keys = [9, 5, 10, 0, 6, 11, -1, 1, 2]
for key in keys:
    avl_tree.insert_key(key)

avl_tree.display_inorder()
