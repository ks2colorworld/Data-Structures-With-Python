import sys
sys.path.append('../binary search tree BST 이진탐색트리')

from my_BST import BST
from my_BT import Node

class AVL(BST):
  def rotateRight(self,Z:Node):
    pass
    # 상위 노드([W])를 [Z]에서 [X]로 변경한다.
    # [W].right에 [Z]
    # if [Z].parent is not None:
      # if [Z].parent.right is [Z]: [Z].parent.right = [W]
      # else: [Z].parent.left = [W]
    # else: [W].parent = None 
    # [Z].left에 b (X.right)
    # return [W]
    
    #          [Z]          >              [X]     
    #       /      \        >            /      \   
    #     [X]      / \      >           a        [Z]  
    #     /  \    / C \     >          / \      /    \ 
    #   a     b             >         / A \    b     / \ 
    #  / \   / \            >                 / \   / C \
    # / A \ / B \           >                / B \
    
  def rotateLeft(self,Z:Node):
    pass
    # 상위 노드([W])를 [Z]에서 [X]로 변경한다.
    # [W].left에 [Z]
    # if [Z].parent is not None:
      # if [Z].parent.right is [Z]: [Z].parent.right = [W]
      # else: [Z].parent.left = [W]
    # else: [W].parent = None 
    # [Z].right에 a (X.left)
    # return [W]
    
    #     [Z]               >          [X]     
    #    /     \            >        /     \         
    #  / \     [X]          >      [Z]       b     
    # / C \   /   \         >      /  \     / \    
    #        a     b        >    / \   a   / B \   
    #       / \   / \       >   / C \ / \     
    #      / A \ / B \      >        / A \        
    