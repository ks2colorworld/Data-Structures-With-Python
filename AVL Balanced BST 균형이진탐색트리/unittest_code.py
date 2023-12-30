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
        
''' New printNode(), nodeHeight() updateNodeHeight()
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
    def setUp(self) -> None:
        #1
        n = Node(3)
        N = AVL()
        #2
        a6=Node(6)
        b9=Node(9)
        c1=Node(1)
        d5=Node(5)
        #set
        self.n,self.N = n,N
        self.a6 = a6
        self.b9 = b9
        self.c1 = c1
        self.d5 = d5
        
    def test_printNode_nodeHeight(self):
        n,N = self.n,self.N
        # print('n:',n.printNode(True)) # node(k:3,p:None,l:None,r:None,height:1)
        self.assertEqual(n.printNode(True), 'node(k:3,p:None,l:None,r:None,height:1)')
        # print('n:', N.printNode(n,True)) # node(k:3,p:None,l:None,r:None,height:1)
        self.assertEqual(N.printNode(n,True), 'node(k:3,p:None,l:None,r:None,height:1)')
        # print('n.heiht',N.nodeHeight(n)) # 1
        self.assertEqual(N.nodeHeight(n), 1)
        nn = None
        # print(N.printNode(nn,True)) # None
        self.assertEqual(N.printNode(nn,True),'None') # str
        # print(N.nodeHeight(nn)) # 0
        self.assertEqual(N.nodeHeight(nn),0)
        
    def test_updateNodeHeight(self):
        a6,b9,c1,d5=self.a6,self.b9,self.c1,self.d5
        N=self.N
        a6.left = b9
        N.updateNodeHeight(b9.parent) # << a6
        # print('a6:',a6.printNode(True)) # node(k:6,p:None,l:9,r:None,height:2)
        self.assertEqual(a6.printNode(True),'node(k:6,p:None,l:9,r:None,height:2)')
        # print('a6.height:',a6.height) # 2
        self.assertEqual(a6.height,2)
        # print('b9.height:',b9.height) # 1
        self.assertEqual(b9.height,1)
        # print('a6.height:',N.nodeHeight(a6)) # 2
        self.assertEqual(N.nodeHeight(a6),2)
        # print('b9.height:',N.nodeHeight(b9)) # 1
        self.assertEqual(N.nodeHeight(b9),1)
        
        a6.right = c1
        N.updateNodeHeight(c1.parent) # << a6
        # print('a6:',a6.printNode(True)) # node(k:6,p:None,l:9,r:1,height:2)
        self.assertEqual(a6.printNode(True),'node(k:6,p:None,l:9,r:1,height:2)')
        # print('a6.height:',a6.height) # 2
        self.assertEqual(a6.height,2)
        # print('c1.height:',c1.height) # 1
        self.assertEqual(c1.height,1)
        # print('a6.height:',N.nodeHeight(a6)) # 2
        self.assertEqual(N.nodeHeight(a6),2)
        # print('c1.height:',N.nodeHeight(c1)) # 1
        self.assertEqual(N.nodeHeight(c1),1)
        
        b9.right = d5
        N.updateNodeHeight(d5.parent) # << b9
        # print('a6:',a6.printNode(True)) # node(k:6,p:None,l:9,r:1,height:3)
        self.assertEqual(a6.printNode(True),'node(k:6,p:None,l:9,r:1,height:3)')
        # print('b9:',b9.printNode(True)) # node(k:9,p:6,l:None,r:5,height:2)
        self.assertEqual(b9.printNode(True),'node(k:9,p:6,l:None,r:5,height:2)')
        # print('c1:',c1.printNode(True)) # node(k:1,p:6,l:None,r:None,height:1)
        self.assertEqual(c1.printNode(True),'node(k:1,p:6,l:None,r:None,height:1)')
        # print('d5:',d5.printNode(True)) # node(k:5,p:9,l:None,r:None,height:1)
        self.assertEqual(d5.printNode(True),'node(k:5,p:9,l:None,r:None,height:1)')
        # print('a6.height:',a6.height) # 3
        self.assertEqual(a6.height,3)
        # print('b9.height:',b9.height) # 2
        self.assertEqual(b9.height,2)
        # print('c1.height:',c1.height) # 1
        self.assertEqual(c1.height,1)
        # print('a6.height:',N.nodeHeight(a6)) # 3
        self.assertEqual(N.nodeHeight(a6),3)
        # print('b9.height:',N.nodeHeight(b9)) # 2
        self.assertEqual(N.nodeHeight(b9),2)
        # print('c1.height:',N.nodeHeight(c1)) # 1
        self.assertEqual(N.nodeHeight(c1),1)


''' rebalance 1
A = AVL()
A.insert(10)
A.insert(5)

print('root.left.height:',A.nodeHeight(A.root.left), 'root.right.height:',A.nodeHeight(A.root.right)) # 1 0
print('A:', A) # [5, 10]
print('A.root:',A.root.printNode(True)) # node(k:10,p:None,l:5,r:None,height:2)
for x in A:
    if A.search(x) is A.root:
        continue
    print(A.search(x).printNode(True))
    

print('----')
A.insert(4)

print('root.left.height:',A.nodeHeight(A.root.left), 'root.right.height:',A.nodeHeight(A.root.right)) # 1 1
print('A:', A) # [4, 5, 10]
print('A.root:',A.root.printNode(True)) # node(k:5,p:None,l:4,r:10,height:2)
for x in A:
    if A.search(x) is A.root:
        continue
    print(A.search(x).printNode(True))

print('----')
A.insert(7)
A.insert(11)
A.insert(14)
A.insert(20)
A.insert(21)

print('root.left.height:',A.nodeHeight(A.root.left), 'root.right.height:',A.nodeHeight(A.root.right)) # 2 3
print('A:', A) # [4, 5, 7, 10, 11, 14, 20, 21]
print('A.root:',A.root.printNode(True)) # node(k:10,p:None,l:5,r:14,height:4)
for x in A:
    if A.search(x) is A.root:
        continue
    print(A.search(x).printNode(True))

# '''

''' rebalance 2
A = AVL()
A.insert(10)
A.insert(5)
A.insert(15)
A.insert(2)
A.insert(7)
A.insert(11)
A.insert(30)
A.insert(4)
A.insert(25)
A.insert(40)

print('A:', A) # [2, 4, 5, 7, 10, 11, 15, 25, 30, 40]
print('A.root:',A.root.printNode(True)) # node(k:10,p:None,l:5,r:15,height:4)
for x in A:
    if A.search(x) is A.root:
        continue
    print(A.search(x).printNode(True))
# '''

class TestAVLRebalanceMethod(unittest.TestCase):
    def test_rebalance1(self):
        A = AVL()
        A.insert(10)
        A.insert(5)

        # print('root.left.height:',A.nodeHeight(A.root.left), 'root.right.height:',A.nodeHeight(A.root.right)) # 1 0
        self.assertEqual(A.nodeHeight(A.root.left),1)
        self.assertEqual(A.nodeHeight(A.root.right),0)
        # print('A:', A) # [5, 10]
        self.assertEqual(str(A),'[5, 10]')
        # print('A.root:',A.root.printNode(True)) # node(k:10,p:None,l:5,r:None,height:2)
        self.assertEqual(A.root.printNode(True),'node(k:10,p:None,l:5,r:None,height:2)')
        for x in A:
            if A.search(x) is A.root:
                continue
            # print(A.search(x).printNode(True))
            s = A.search(x).printNode(True)
            match x:
                case 5:
                    self.assertEqual(s,'node(k:5,p:10,l:None,r:None,height:1)')
            

        # print('----')
        A.insert(4)

        # print('root.left.height:',A.nodeHeight(A.root.left), 'root.right.height:',A.nodeHeight(A.root.right)) # 1 1
        self.assertEqual(A.nodeHeight(A.root.left),1)
        self.assertEqual(A.nodeHeight(A.root.right),1)
        # print('A:', A) # [4, 5, 10]
        self.assertEqual(str(A),'[4, 5, 10]')
        # print('A.root:',A.root.printNode(True)) # node(k:5,p:None,l:4,r:10,height:2)
        self.assertEqual(A.root.printNode(True),'node(k:5,p:None,l:4,r:10,height:2)')
        for x in A:
            if A.search(x) is A.root:
                continue
            # print(A.search(x).printNode(True))
            s = A.search(x).printNode(True)
            match x:
                case 4:
                    self.assertEqual(s,'node(k:4,p:5,l:None,r:None,height:1)')
                case 10:
                    self.assertEqual(s,'node(k:10,p:5,l:None,r:None,height:1)')

        # print('----')
        A.insert(7)
        A.insert(11)
        A.insert(14)
        A.insert(20)
        A.insert(21)

        # print('root.left.height:',A.nodeHeight(A.root.left), 'root.right.height:',A.nodeHeight(A.root.right)) # 2 3
        self.assertEqual(A.nodeHeight(A.root.left),2)
        self.assertEqual(A.nodeHeight(A.root.right),3)
        # print('A:', A) # [4, 5, 7, 10, 11, 14, 20, 21]
        self.assertEqual(str(A),'[4, 5, 7, 10, 11, 14, 20, 21]')
        # print('A.root:',A.root.printNode(True)) # node(k:10,p:None,l:5,r:14,height:4)
        self.assertEqual(A.root.printNode(True),'node(k:10,p:None,l:5,r:14,height:4)')
        for x in A:
            if A.search(x) is A.root:
                continue
            # print(A.search(x).printNode(True))
            s = A.search(x).printNode(True)
            match x:
                case 4:
                    self.assertEqual(s,'node(k:4,p:5,l:None,r:None,height:1)')
                case 5:
                    self.assertEqual(s,'node(k:5,p:10,l:4,r:7,height:2)')
                case 7:
                    self.assertEqual(s,'node(k:7,p:5,l:None,r:None,height:1)')
                case 11:
                    self.assertEqual(s,'node(k:11,p:14,l:None,r:None,height:1)')
                case 14:
                    self.assertEqual(s,'node(k:14,p:10,l:11,r:20,height:3)')
                case 20:
                    self.assertEqual(s,'node(k:20,p:14,l:None,r:21,height:2)')
                case 21:
                    self.assertEqual(s,'node(k:21,p:20,l:None,r:None,height:1)')

        
''' insert
A = AVL()
A.insert(10)
A.insert(5)
A.insert(15)
A.insert(2)
A.insert(7)
A.insert(11)
A.insert(30)
A.insert(4)
A.insert(25)
A.insert(40)

print('A:', A) # [2, 4, 5, 7, 10, 11, 15, 25, 30, 40]

print('----')
A.insert(27)

print('A:', A) # [2, 4, 5, 7, 10, 11, 15, 25, 27, 30, 40]
print('[30]:', A.search(27).parent.printNode(True)) # 30 # node(k:30,p:25,l:27,r:40,height:2)
print('[27]:', A.search(27).printNode(True)) # 27 # node(k:27,p:30,l:None,r:None,height:1)

print('----')
A.insert(28)

print('A:', A) # 
print('[27]:', A.search(28).parent.printNode(True)) # 27 # node(k:27,p:30,l:None,r:28,height:2)
print('[28]:', A.search(28).printNode(True)) # 28 # node(k:28,p:27,l:None,r:None,height:1)

# '''

class TestAVLInsertMethod(unittest.TestCase):
    def setUp(self) -> None:
        A = AVL()
        A.insert(10)
        A.insert(5)
        A.insert(15)
        A.insert(2)
        A.insert(7)
        A.insert(11)
        A.insert(30)
        A.insert(4)
        A.insert(25)
        A.insert(40)
        self.A = A
    
    def test_insert(self):
        A = self.A
        
        # print('A:', A) # [2, 4, 5, 7, 10, 11, 15, 25, 30, 40]
        self.assertEqual(str(A),'[2, 4, 5, 7, 10, 11, 15, 25, 30, 40]')

        # print('----')
        A.insert(27)

        # print('A:', A) # [2, 4, 5, 7, 10, 11, 15, 25, 27, 30, 40]
        self.assertEqual(str(A),'[2, 4, 5, 7, 10, 11, 15, 25, 27, 30, 40]')
        # print('[30]:', A.search(27).parent.printNode(True)) # 30 # node(k:30,p:25,l:27,r:40,height:2)
        self.assertEqual(A.search(27).parent.printNode(True),'node(k:30,p:25,l:27,r:40,height:2)')
        # print('[27]:', A.search(27).printNode(True)) # 27 # node(k:27,p:30,l:None,r:None,height:1)
        self.assertEqual(A.search(27).printNode(True),'node(k:27,p:30,l:None,r:None,height:1)')

        # print('----')
        A.insert(28)

        # print('A:', A) # [2, 4, 5, 7, 10, 11, 15, 25, 27, 28, 30, 40]
        self.assertEqual(str(A),'[2, 4, 5, 7, 10, 11, 15, 25, 27, 28, 30, 40]')
        # print('[27]:', A.search(28).parent.printNode(True)) # 27 # node(k:27,p:30,l:None,r:28,height:2)
        self.assertEqual(A.search(28).parent.printNode(True),'node(k:27,p:30,l:None,r:28,height:2)')
        # print('[28]:', A.search(28).printNode(True)) # 28 # node(k:28,p:27,l:None,r:None,height:1)
        self.assertEqual(A.search(28).printNode(True),'node(k:28,p:27,l:None,r:None,height:1)')

# ''' delete

# '''

    class TestAVLDeleteMethod(unittest.TestCase):
        pass
if __name__ == '__main__':
    unittest.main()
