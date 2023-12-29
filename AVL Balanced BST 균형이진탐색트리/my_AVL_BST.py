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
    # set each Node's height to leafNode 
      # 삽입되는 노드의 부모노드들을 추적하여 각 노드들의 height를 +1씩 증가시킨다.
      # Node 클래스에 height를 추가한다. 
      
    # find X,Y,Z 
      # Z : left, right의 노드의 높이(height)차이가 2 이상 차이나는 첫번째 부모 노드
      # Y : 삽입된 v 노드가 포함된 Z.left (혹은 Z.right) 노드 
      # X : 삽입된 v 노드가 포함된 Y.left (혹은 Y.right) 노드 
      
    # W = rebalance X,Y,Z 
      # W = rebalance 후 가장 상위 노드
      # Y가 Z.left 이면서, X가 Y.left 일 때 >> rotateRight(Z) 1회
      # Y가 Z.right 이면서, X가 Y.right 일 때 >> rotateLeft(Z) 1회
      # Y가 Z.left 이면서, X가 Y.right 일 때 >> rotateLeft(Y) 1회 >> rotateRight(Z) 1회
      # Y가 Z.right 이면서, X가 Y.right 일 때 >> rotateLeft(Z) 1회
      # Y가 Z.right 이면서, X가 Y.left 일 때 >> rotateRight(Y) 1회 >> rotateLeft(Z) 1회
    
    # Z is root Node? self.root = W 
      # 루트 노드 변경 