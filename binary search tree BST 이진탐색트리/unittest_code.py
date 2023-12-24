import unittest
from my_BT import Node
from my_BST import BST

class TestBinaryTreeMethods(unittest.TestCase):
  def setUp(_):
    _.a6 = Node(6)
    _.b9 = Node(9)
    _.c1 = Node(1)
    _.d5 = Node(5)

    _.a6.left = _.b9
    _.a6.right = _.c1
    _.b9.right = _.d5
    
    _.b9.parent = _.a6
    _.c1.parent = _.a6
    _.b9.left = None
    _.d5.parent = _.b9

  def test_preorder(_): #1
    _.assertEqual(_.a6.preorder(), [6, 9, 5, 1])
    _.assertEqual(_.b9.preorder(), [9, 5])
    _.assertEqual(_.c1.preorder(), [1])
    _.assertEqual(_.d5.preorder(), [5])

  def test_inorder(_): #2
    _.assertEqual(_.a6.inorder(), [9, 5, 6, 1])
    _.assertEqual(_.b9.inorder(), [9, 5])
    _.assertEqual(_.c1.inorder(), [1])
    _.assertEqual(_.d5.inorder(), [5])

class TestBinaryTreeWithoutParentMethods(unittest.TestCase):
  def setUp(_):
    _.a6 = Node(6)
    _.b9 = Node(9)
    _.c1 = Node(1)
    _.d5 = Node(5)

    _.a6.left = _.b9
    _.a6.right = _.c1
    _.b9.right = _.d5

  def test_preorder(_): #3
    _.assertEqual(_.a6.preorder(), [6, 9, 5, 1])
    _.assertEqual(_.b9.preorder(), [9, 5])
    _.assertEqual(_.c1.preorder(), [1])
    _.assertEqual(_.d5.preorder(), [5])

  def test_inorder(_): #4
    _.assertEqual(_.a6.inorder(), [9, 5, 6, 1])
    _.assertEqual(_.b9.inorder(), [9, 5])
    _.assertEqual(_.c1.inorder(), [1])
    _.assertEqual(_.d5.inorder(), [5])
    
class TestPreoderInoder(unittest.TestCase):
  def setUp(_) -> None:
    _.root = Node(6, left=Node(9, right=Node(5)), right=Node(1))
    return super().setUp()
  
  def test_preorder(_):#5
    _.assertEqual(_.root.preorder(), [6, 9, 5, 1])

  def test_inorder(_):#6
    _.assertEqual(_.root.inorder(), [9, 5, 6, 1])

class TestNodeInitNew(unittest.TestCase):
  def setUp(_) -> None:
    _.root = Node('F',\
        left=Node('B',left=Node('A'),\
                      right=Node('D', left=Node('C'),\
                                      right=Node('E'))),\
        right=Node('G',right=Node('I',left=Node('H'))))
    return super().setUp()
  
  def test_preorder(_):#7
      _.assertEqual(_.root.preorder(), ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H'])

  def test_inorder(_):#8
      _.assertEqual(_.root.inorder(), ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])

  def test_iteration_inorder(_):#9
      expected_result = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
      actual_result = [x for x in _.root]
      _.assertEqual(actual_result, expected_result)

class TestBSTInsert(unittest.TestCase):
  #10
  def test_insert_single_element(_):
    bst = BST()
    bst.insert(2)
    _.assertEqual(str(bst), "[2]")

  #11
  def test_insert_multiple_elements(_):
    bst = BST()
    elements = [2, 40, 20, 15, 5, 61, 32, 12]
    for element in elements:
      bst.insert(element)
    _.assertEqual(str(bst), "[2, 5, 12, 15, 20, 32, 40, 61]")


class TestBSTInitWithNode_find_loc_search_insert_Methods(unittest.TestCase):

  def setUp(_):
    root = Node(15,\
      left=Node(4,  left=Node(2)),\
      right=Node(20,left=Node(17,\
                                right=Node(19)),\
                    right=Node(32)))
    #      15
    #     /   \
    #    4     20
    #   /     /  \
    #  2    17    32
    #         \
    #          19
    _.bst = BST(root)

  def test_inorder_iteration(_):
    expected_result = [2, 4, 15, 17, 19, 20, 32]
    actual_result = [x for x in _.bst]
    _.assertEqual(actual_result, expected_result)

  def test_len_method(_):
    _.assertEqual(len(_.bst), 7)

  def test_find_loc_method_existing_value(_):
    found_node = _.bst.find_loc(17)
    _.assertEqual(found_node.key, 17)

  def test_find_loc_method_nonexistent_value(_):
    found_node = _.bst.find_loc(1)
    _.assertEqual(found_node.key, 2) 

  def test_search_method_existing_value(_):
    found_node = _.bst.search(17)
    _.assertEqual(found_node.key, 17)

  def test_search_method_nonexistent_value(_):
    found_node = _.bst.search(1)
    _.assertIsNone(found_node)

  def test_insert_method_existing_value(_):
    _.assertFalse(_.bst.insert(17))  # Should return False because the value already exists

  def test_insert_method_nonexistent_value(_):
    _.assertTrue(_.bst.insert(1))  # Should return True because the value is inserted

class TestBST_deleteNode_Methods(unittest.TestCase):
  def setUp(_):
    _.bst = BST()
    _.bst.insert(2)
    _.bst.insert(40)
    _.bst.insert(20)
    _.bst.insert(15)
    _.bst.insert(5)
    _.bst.insert(61)
    _.bst.insert(32)
    _.bst.insert(12)

    #     2
    #       \
    #        40
    #       /  \
    #      20   61
    #     /  \
    #    15  32
    #   /
    #  5
    #   \
    #   12
    
  def test_deleteNodeByCopying(_):
    deleted_node = _.bst.deleteNodeByCopying(_.bst.search(2))
    expected_result_str = "[5, 12, 15, 20, 32, 40, 61]"
    _.assertEqual(deleted_node.key,2)
    _.assertEqual(str(_.bst), expected_result_str)

  def test_deleteNodeByMerging(_):
    deleted_node = _.bst.deleteNodeByMerging(_.bst.search(15))
    expected_result_str = "[2, 5, 12, 20, 32, 40, 61]"
    _.assertEqual(deleted_node.key,15)
    _.assertEqual(str(_.bst), expected_result_str)

class TestBST_deleteKey_Methods(unittest.TestCase):
  def setUp(_):
    _.bst = BST()
    _.bst.insert(15)
    _.bst.insert(4)
    _.bst.insert(20)
    _.bst.insert(17)
    _.bst.insert(19)
    _.bst.insert(32)
    _.bst.insert(2)
    _.bst.insert(18)
    _.bst.insert(16)
  
    #      15
    #     /   \
    #    4     20
    #   /     /  \
    #  2    17    32
    #       / \
    #     16   19
    #         / 
    #       18 
    
  def test_deleteByCopying(_):
    deleted_key = _.bst.deleteByCopying(20)
    expected_result_str = "[2, 4, 15, 16, 17, 18, 19, 32]"
    _.assertEqual(str(_.bst), expected_result_str)
    _.assertEqual(deleted_key,20)

  def test_deleteByMerging(_):
    deleted_key = _.bst.deleteByMerging(20)
    expected_result_str = "[2, 4, 15, 16, 17, 18, 19, 32]"
    _.assertEqual(str(_.bst), expected_result_str)
    _.assertEqual(deleted_key,20)

  def test_deleteByCopyingFail(_):
    deleted_key = _.bst.deleteByCopying(1)
    expected_result_str = "[2, 4, 15, 16, 17, 18, 19, 20, 32]"
    _.assertEqual(str(_.bst), expected_result_str)
    _.assertIsNone(deleted_key)

  def test_deleteByMergingFail(_):
    deleted_key = _.bst.deleteByMerging(1)
    expected_result_str = "[2, 4, 15, 16, 17, 18, 19, 20, 32]"
    _.assertEqual(str(_.bst), expected_result_str)
    _.assertIsNone(deleted_key)

if __name__ == '__main__':
    unittest.main()
