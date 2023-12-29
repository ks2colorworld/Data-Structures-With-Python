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
    