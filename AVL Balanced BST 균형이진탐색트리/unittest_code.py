import unittest
from my_AVL_BST import AVL
from my_AVL_BST import Node

# ''' rotateRight 
L = AVL(\
    Node('Z',\
        left=Node('X',\
            left=Node('a',\
                left=Node('[A]')),\
            right=Node('b',\
                right=Node('[B]'))),\
        right=Node('[C]')))
print('L:',L) # ['[A]', 'a', 'X', 'b', '[B]', 'Z', '[C]']
Z = L.root
W = L.rotateRight(Z) 
print('W:',L.printNode(W)) # node(k:X,p:None,l:a,r:Z)
L.root = W
print('Z:', L.printNode(W.right)) # node(k:Z,p:X,l:b,r:[C])
print('a:', L.printNode(W.left)) # node(k:a,p:X,l:[A],r:None)
print('b:', L.printNode(W.right.left)) # node(k:b,p:Z,l:None,r:[B])
print('L:',L) # ['[A]', 'a', 'X', 'b', '[B]', 'Z', '[C]']
# '''

class TestAVLRotateRightMethod(unittest.TestCase):
    pass

''' rotateLeft
# '''

class TestAVLRotateLeftMethod(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
