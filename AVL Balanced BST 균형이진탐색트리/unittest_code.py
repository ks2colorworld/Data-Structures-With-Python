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
    def setUp(self) -> None:
        L = AVL(\
            Node('Z',\
                left=Node('X',\
                    left=Node('a',\
                        left=Node('[A]')),\
                    right=Node('b',\
                        right=Node('[B]'))),\
                right=Node('[C]')))
        self.L = L
    
    def test_rotateRight(self):
        # self.skipTest('add node height issue')
        L = self.L
        # print('L:',L) # ['[A]', 'a', 'X', 'b', '[B]', 'Z', '[C]']
        self.assertEqual(str(L), "['[A]', 'a', 'X', 'b', '[B]', 'Z', '[C]']")
        Z = L.root
        W = L.rotateRight(Z) 
        # print('W:',L.printNode(W)) # node(k:X,p:None,l:a,r:Z)
        self.assertEqual(L.printNode(W), 'node(k:X,p:None,l:a,r:Z)')
        L.root = W
        # print('Z:', L.printNode(W.right)) # node(k:Z,p:X,l:b,r:[C])
        self.assertEqual(L.printNode(W.right),'node(k:Z,p:X,l:b,r:[C])')
        # print('a:', L.printNode(W.left)) # node(k:a,p:X,l:[A],r:None)
        self.assertEqual(L.printNode(W.left),'node(k:a,p:X,l:[A],r:None)')
        # print('b:', L.printNode(W.right.left)) # node(k:b,p:Z,l:None,r:[B])
        self.assertEqual(L.printNode(W.right.left),'node(k:b,p:Z,l:None,r:[B])')
        # print('L:',L) # ['[A]', 'a', 'X', 'b', '[B]', 'Z', '[C]']
        self.assertEqual(str(L), "['[A]', 'a', 'X', 'b', '[B]', 'Z', '[C]']")
    
''' rotateLeft
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
    def setUp(self) -> None:
        L = AVL(\
            Node('Z',\
                left=Node('[C]'),\
                right=Node('X',\
                    left=Node('a',\
                        left=Node('[A]')),\
                    right=Node('b',\
                        right=Node('[B]')))))
        self.L = L

    def test_rotateLeft(self):
        # self.skipTest('add node height issue')
        L = self.L
        # print('L:',L) # ['[C]', 'Z', '[A]', 'a', 'X', 'b', '[B]']
        self.assertEqual(str(L), "['[C]', 'Z', '[A]', 'a', 'X', 'b', '[B]']")
        Z = L.root
        W = L.rotateLeft(Z) 
        # print('W:',L.printNode(W)) # node(k:X,p:None,l:Z,r:b)
        self.assertEqual(L.printNode(W),'node(k:X,p:None,l:Z,r:b)')
        L.root = W
        # print('Z:', L.printNode(W.left)) # node(k:Z,p:X,l:[C],r:a)
        self.assertEqual(L.printNode(W.left),'node(k:Z,p:X,l:[C],r:a)')
        # print('a:', L.printNode(W.left.right)) # node(k:a,p:Z,l:[A],r:None)
        self.assertEqual(L.printNode(W.left.right),'node(k:a,p:Z,l:[A],r:None)')
        # print('b:', L.printNode(W.right)) # node(k:b,p:X,l:None,r:[B])
        self.assertEqual(L.printNode(W.right),'node(k:b,p:X,l:None,r:[B])')
        # print('L:',L) # ['[C]', 'Z', '[A]', 'a', 'X', 'b', '[B]']
        self.assertEqual(str(L), "['[C]', 'Z', '[A]', 'a', 'X', 'b', '[B]']")
        
# ''' New printNode(), nodeHeight() updateNodeHeight()
    n = Node(3)
    print('n:',n.printNode(True)) # node(k:3,p:None,l:None,r:None,height:1)
    N = AVL()
    print('n:', N.printNode(n,True)) # node(k:3,p:None,l:None,r:None,height:1)
    print('n.heiht',N.nodeHeight(n)) # 1
    nn = None
    print(N.printNode(nn,True)) # None
    print(N.nodeHeight(nn)) # 0
    
    a6=Node(6)
    b9=Node(9)
    c1=Node(1)
    d5=Node(5)

    a6.left = b9
    N.updateNodeHeight(b9.parent) # << a6
    print('a6:',a6.printNode(True)) # node(k:6,p:None,l:9,r:None,height:2)
    print('a6.height:',a6.height) # 2
    print('b9.height:',b9.height) # 1
    print('a6.height:',N.nodeHeight(a6)) # 2
    print('b9.height:',N.nodeHeight(b9)) # 1
    
    a6.right = c1
    N.updateNodeHeight(c1.parent) # << a6
    print('a6:',a6.printNode(True)) # node(k:6,p:None,l:9,r:1,height:2)
    print('a6.height:',a6.height) # 2
    print('c1.height:',c1.height) # 1
    print('a6.height:',N.nodeHeight(a6)) # 2
    print('c1.height:',N.nodeHeight(c1)) # 1
    
    b9.right = d5
    N.updateNodeHeight(d5.parent) # << b9
    print('a6:',a6.printNode(True)) # node(k:6,p:None,l:9,r:1,height:3)
    print('b9:',b9.printNode(True)) # node(k:9,p:6,l:None,r:5,height:2)
    print('c1:',c1.printNode(True)) # node(k:1,p:6,l:None,r:None,height:1)
    print('d5:',d5.printNode(True)) # node(k:5,p:9,l:None,r:None,height:1)
    print('a6.height:',a6.height) # 3
    print('b9.height:',b9.height) # 2
    print('c1.height:',c1.height) # 1
    print('a6.height:',N.nodeHeight(a6)) # 3
    print('b9.height:',N.nodeHeight(b9)) # 2
    print('c1.height:',N.nodeHeight(c1)) # 1

    #    6
    #   / \
    #  9   1
    #   \
    #    5
# '''

class TestAVLUtilFuncMethod(unittest.TestCase):
    pass

# ''' insert

# '''

class TestAVLInsertMethod(unittest.TestCase):
    pass

if __name__ == '__main__':
    unittest.main()
