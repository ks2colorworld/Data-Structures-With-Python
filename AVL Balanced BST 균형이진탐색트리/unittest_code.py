import unittest
from my_AVL_BST import AVL
from my_AVL_BST import Node

''' rotateRight 
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

#          [Z]          >              [X]     
#       /      \        >            /      \   
#     [X]      / \      >           a        [Z]  
#     /  \    / C \     >          / \      /    \ 
#   a     b             >         / A \    b     / \ 
#  / \   / \            >                 / \   / C \
# / A \ / B \           >                / B \

class TestAVLRotateRightMethod(unittest.TestCase):
    pass

# ''' rotateLeft
L = AVL(\
    Node('Z',\
        left=Node('[C]'),\
        right=Node('X',\
            left=Node('a',\
                left=Node('[A]')),\
            right=Node('b',\
                right=Node('[B]')))))
print('L:',L) # ['[C]', 'Z', '[A]', 'a', 'X', 'b', '[B]']
Z = L.root
W = L.rotateLeft(Z) 
print('W:',L.printNode(W)) # node(k:X,p:None,l:Z,r:b)
L.root = W
print('Z:', L.printNode(W.left)) # node(k:Z,p:X,l:[C],r:a)
print('a:', L.printNode(W.left.right)) # node(k:a,p:Z,l:[A],r:None)
print('b:', L.printNode(W.right)) # node(k:b,p:X,l:None,r:[B])
print('L:',L) # ['[C]', 'Z', '[A]', 'a', 'X', 'b', '[B]']
# '''

#     [Z]               >          [X]     
#    /     \            >        /     \         
#  / \     [X]          >      [Z]       b     
# / C \   /   \         >      /  \     / \    
#        a     b        >    / \   a   / B \   
#       / \   / \       >   / C \ / \     
#      / A \ / B \      >        / A \        

class TestAVLRotateLeftMethod(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
