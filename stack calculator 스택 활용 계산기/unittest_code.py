import unittest
from calculator import change_to_postfix,calculate_postfix,calulate_infix

# """ 
# infix = '1+2*3' # 123*+ # 7
# infix = '(1*2)+3' # 12*3+ # 5
# infix = '(1+2)*3' # 12+3* # 9
# infix = '(1+2)*3+7' # 12+3*7+ # 16
# infix = '(1+2)+3*4/5+(6*7-8)' # 12+34*5/67*8-++ # 39.4
infix = '(1*2-1)+3' 
# print(change_to_postfix(infix, True))
# print(change_to_postfix(infix, False))
print(calulate_infix(infix, False))

# print('postfix : ', change_to_postfix(infix, True))
# print('postfix : ', change_to_postfix(infix, False))
# print('result : ', calulate_infix(infix, True))
# print('result : ', calulate_infix(infix, False))
# """

# (1*2-1)+3 = 4
class Test6(unittest.TestCase):
  def setUp(self) -> None:
    infix = '(1*2-1)+3' # 12*1-3+  # 4
    postfix_result = '12*1-3+'
    answer = 4
    
    self.infix = infix
    self.postfix_result = postfix_result
    self.answer = answer 
    return super().setUp()
  
  def test_1(self):
    infix = self.infix
    postfix_result = self.postfix_result
    answer = self.answer
    
    postfix = change_to_postfix(infix, False) # stack
    
    # print('postfix : ', change_to_postfix(infix, False))
    self.assertEqual(''.join(map(str, postfix)), postfix_result)
    # self.assertEqual(postfix, '123*+')
    
    # print('result : ', calulate_infix(infix, False))
    # self.assertEqual(calulate_infix(infix, False), answer)
    self.assertEqual(calculate_postfix(postfix, False), answer)

# (1+2)+3*4/5+(6*7-8) = 39.4
class Test5(unittest.TestCase):
  def setUp(self) -> None:
    infix = '(1+2)+3*4/5+(6*7-8)' # 12+34*5/67*8-++ # 39.4
    postfix_result = '12+34*5/67*8-++'
    answer = 39.4
    
    self.infix = infix
    self.postfix_result = postfix_result
    self.answer = answer 
    return super().setUp()
  
  def test_1(self):
    infix = self.infix
    postfix_result = self.postfix_result
    answer = self.answer
    
    postfix = change_to_postfix(infix, False) # stack
    
    # print('postfix : ', change_to_postfix(infix, False))
    self.assertEqual(''.join(map(str, postfix)), postfix_result)
    # self.assertEqual(postfix, '123*+')
    
    # print('result : ', calulate_infix(infix, False))
    # self.assertEqual(calulate_infix(infix, False), answer)
    self.assertEqual(calculate_postfix(postfix, False), answer)

# (1+2)*3+7 = 16
class Test4(unittest.TestCase):
  def setUp(self) -> None:
    infix = '(1+2)*3+7' # 12+3*7+ # 16
    postfix_result = '12+3*7+'
    answer = 16
    
    self.infix = infix
    self.postfix_result = postfix_result
    self.answer = answer 
    return super().setUp()
  
  def test_1(self):
    infix = self.infix
    postfix_result = self.postfix_result
    answer = self.answer
    
    postfix = change_to_postfix(infix, False) # stack
    
    # print('postfix : ', change_to_postfix(infix, False))
    self.assertEqual(''.join(map(str, postfix)), postfix_result)
    # self.assertEqual(postfix, '123*+')
    
    # print('result : ', calulate_infix(infix, False))
    # self.assertEqual(calulate_infix(infix, False), answer)
    self.assertEqual(calculate_postfix(postfix, False), answer)

# (1+2)*3 = 9
class Test3(unittest.TestCase):
  def setUp(self) -> None:
    infix = '(1+2)*3' # 12+3* # 9
    postfix_result = '12+3*'
    answer = 9
    
    self.infix = infix
    self.postfix_result = postfix_result
    self.answer = answer 
    return super().setUp()
  
  def test_1(self):
    infix = self.infix
    postfix_result = self.postfix_result
    answer = self.answer
    
    postfix = change_to_postfix(infix, False) # stack
    
    # print('postfix : ', change_to_postfix(infix, False))
    self.assertEqual(''.join(map(str, postfix)), postfix_result)
    # self.assertEqual(postfix, '123*+')
    
    # print('result : ', calulate_infix(infix, False))
    # self.assertEqual(calulate_infix(infix, False), answer)
    self.assertEqual(calculate_postfix(postfix, False), answer)

# (1*2)+3 = 5
class Test2(unittest.TestCase):
  def setUp(self) -> None:
    infix = '(1*2)+3' # 12*3+ # 5
    postfix_result = '12*3+'
    answer = 5
    
    self.infix = infix
    self.postfix_result = postfix_result
    self.answer = answer 
    return super().setUp()
  
  def test_1(self):
    infix = self.infix
    postfix_result = self.postfix_result
    answer = self.answer
    
    postfix = change_to_postfix(infix, False) # stack
    
    # print('postfix : ', change_to_postfix(infix, False))
    self.assertEqual(''.join(map(str, postfix)), postfix_result)
    # self.assertEqual(postfix, '123*+')
    
    # print('result : ', calulate_infix(infix, False))
    # self.assertEqual(calulate_infix(infix, False), answer)
    self.assertEqual(calculate_postfix(postfix, False), answer)

# 1+2*3 = 7
class Test1(unittest.TestCase):
  def setUp(self) -> None:
    infix = '1+2*3' # 123*+ # 7
    postfix_result = '123*+'
    answer = 7.0
    
    self.infix = infix
    self.postfix_result = postfix_result
    self.answer = answer 
    return super().setUp()
  
  def test_1(self):
    infix = self.infix
    postfix_result = self.postfix_result
    answer = self.answer
    
    postfix = change_to_postfix(infix, False) # stack
    
    # print('postfix : ', change_to_postfix(infix, False))
    self.assertEqual(''.join(map(str, postfix)), postfix_result)
    # self.assertEqual(postfix, '123*+')
    
    # print('result : ', calulate_infix(infix, False))
    # self.assertEqual(calulate_infix(infix, False), answer)
    self.assertEqual(calculate_postfix(postfix, False), answer)

if __name__ == '__main__':
    unittest.main()
