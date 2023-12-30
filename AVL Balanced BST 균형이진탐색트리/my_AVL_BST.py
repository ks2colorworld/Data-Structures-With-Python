import sys
sys.path.append('../binary search tree BST 이진탐색트리')

from my_BST import BST
from my_BT import Node

class AVL(BST):
  def rotateRight(self,Z:Node):
    if Z is None: return None
    if Z.left is None: return None
    X = Z.left  # not None
    b = X.right # can be None
    # 상위 노드([W])를 [Z]에서 [X]로 변경한다.
    W = X
    pt = Z.parent
    if pt is not None: 
      if pt.right is Z: pt.right = W # also set W.parent = pt
      else: pt.left = W # also set W.parent = pt
    else: W.parent = None # not set root = W (Set in the code that called rotateRight())
    W.right = Z # also set Z.parent = W
    # [Z].left에 b (X.right)
    Z.left = b # also set b.parent = Z
    self.updateNodeHeight(Z)
    return W
    
    #          [Z]          >              [X]     
    #       /      \        >            /      \   
    #     [X]      / \      >           a        [Z]  
    #     /  \    / C \     >          / \      /    \ 
    #   a     b             >         / A \    b     / \ 
    #  / \   / \            >                 / \   / C \
    # / A \ / B \           >                / B \
    
  def rotateLeft(self,Z:Node):
    if Z is None: return None
    if Z.right is None: return None
    X = Z.right  # not None
    a = X.left # can be None
    # 상위 노드([W])를 [Z]에서 [X]로 변경한다.
    W = X
    pt = Z.parent
    if pt is not None: 
      if pt.right is Z: pt.right = W # also set W.parent = pt
      else: pt.left = W # also set W.parent = pt
    else: W.parent = None # not set root = W (Set in the code that called rotateLeft())
    W.left = Z # also set Z.parent = W
    # [Z].right에 a (X.left)
    Z.right = a # also set a.parent = Z
    self.updateNodeHeight(Z)
    return W
    
    #     [Z]               >          [X]     
    #    /     \            >        /     \         
    #  / \     [X]          >      [Z]       b     
    # / C \   /   \         >      /  \     / \    
    #        a     b        >    / \   a   / B \   
    #       / \   / \       >   / C \ / \     
    #      / A \ / B \      >        / A \        
    
  def insert(self, key):
    v = super().insert(key)
    if v is None:
      return None
    print('insert:',v.printNode(True))
    
    # set each Node's height to leafNode 
      # 삽입되는 노드의 부모노드들을 추적하여 각 노드들의 height를 +1씩 증가시킨다.
      # Node 클래스에 height를 추가한다. 
    self.updateNodeHeight(v.parent)
      
    # find X,Y,Z 
      # Z : left, right의 노드의 높이(height)차이가 2 이상 차이나는 첫번째 부모 노드
      # Y : 삽입된 v 노드가 포함된 Z.left (혹은 Z.right) 노드 
      # X : 삽입된 v 노드가 포함된 Y.left (혹은 Y.right) 노드 
    a = v.parent
    if a is None: return v # v is aleady root 
    
    X = v
    Y = X.parent # not None
    Z = Y.parent # can be None
    if Z is None: return v # 0->1
    
    print('---1---')
    needForRebalance = False
    while Z is not None: # to root-node
      heightDiff = self.nodeHeight(Z.left) - self.nodeHeight(Z.right)
      if 1 < abs(heightDiff): # 그 차이가 2, -2 이상 나면
        print('heightDiff:',heightDiff)
        needForRebalance = True
        break
      X = Y # up one node
      Y = X.parent
      if Y is None: return v
      Z = Y.parent
      if Z is None: return v

    print('---2-1---')
    if not needForRebalance: return v # no need for rebalance
      
    print('---2-2---')
    # W = rebalance X,Y,Z 
    W = self.rebalance(X,Y,Z)
    print('W:',W.printNode(True))
    while True:
      Z = W.parent
      if Z is None: # W is root
        print('W is root')
        self.root = W
        return v 
      heightDiff = self.nodeHeight(Z.left) - self.nodeHeight(Z.right)
      if abs(heightDiff) < 2: # 그 차이가 1, 0이면
        break
      if 1 < heightDiff: # Z.left
        Y = Z.left
      else: Y = Z.right
      heightDiff = self.nodeHeight(Y.left) - self.nodeHeight(Y.right)
      if 1 < heightDiff: # Y.left
        X = Y.left
      else: X = Y.right
      W = self.rebalance(X,Y,Z)
      print('W:',W.printNode(True))
      
    print('---3-1---')
    if W is None: return v # something is wrong
    
    print('---3-2---')
    # Z is root Node? self.root = W 
      # 루트 노드 변경 
    # (불필요) if Z.parent is None: self.root = W
    return v
  
  def rebalance(self,X:Node,Y:Node,Z:Node):
    if X is None or Y is None or Z is None: return None
    
    # W = rebalance 후 가장 상위 노드
    W = None
    # Y가 Z.left 이면서, X가 Y.left 일 때 >> rotateRight(Z) 1회
    if Y is Z.left and X is Y.left: 
      W = self.rotateRight(Z)
    # Y가 Z.left 이면서, X가 Y.right 일 때 >> rotateLeft(Y) 1회 >> rotateRight(Z) 1회
    elif Y is Z.left and X is Y.right:
      self.rotateLeft(Y)
      W = self.rotateRight(Z)
    # Y가 Z.right 이면서, X가 Y.right 일 때 >> rotateLeft(Z) 1회
    elif Y is Z.right and X is Y.right:
      W = self.rotateLeft(Z)
    # Y가 Z.right 이면서, X가 Y.left 일 때 >> rotateRight(Y) 1회 >> rotateLeft(Z) 1회
    elif Y is Z.right and X is Y.left:
      self.rotateRight(Y)
      W = self.rotateLeft(Z)
    
    if W is None: return None # something is wrong
    return W
  
  def nodeHeight(self,node:Node):
    if node is None: return 0
    return node.height
  
  def updateNodeHeight(self,node:Node):
    h = 0 if node is None else node.height
    if node is not None:
      node.height = 1 + max(self.nodeHeight(node.left),self.nodeHeight(node.right))
    else: return
    if node.height == h: return
    
    pt:Node = node.parent
    if pt is None: return
    while pt is not None:
      pt.height = 1 + max(self.nodeHeight(pt.left),self.nodeHeight(pt.right))
      pt = pt.parent
  
  def printNode(self, x: Node, withHeight:bool=False):
    if x is None:
      return 'None'
    # return x.printNode() if withHeight else super().printNode(x)
    return x.printNode(withHeight)
  