import unittest
from calculator import add_comma, change_to_postfix,calculate_postfix,calulate_infix, remove_comma

""" (커밋할 때 주석해제 처리) 
# infix = '1+2*3' # 123*+ # 7
# infix = '(1*2)+3' # 12*3+ # 5
# infix = '(1+2)*3' # 12+3* # 9
# infix = '(1+2)*3+7' # 12+3*7+ # 16
# infix = '(1+2)+3*4/5+(6*7-8)' # 12+34*5/67*8-++ # 39.4
# infix = '(1*2-1)+3' 

# 두자리 이상 숫자 대응 
# infix = '12+3' # 123+ # 15
# infix = '(12*24)+35' # 1224*35+ # 323.0
# infix = '(12+245)*367' # 12245+367* # 94319
# infix = '(1234+2456)*323+71' # 12342456+323*71+ # 1191941.0
# infix = '(1234+2122)+33*432/532+(623*744-811)' # 12342122+33432*532/623744*811-++ # 466083.7969924812

# infix = '12,000+3' # 
infix = '12,000+3,123' # 15,123.0
# infix = '12,000,000+3,123' # 

# infix = '2/3' 
# (){}[] 괄호 대응 
# XX infix = '{12+245}*367' # 12245+367* # 94319

# print(change_to_postfix(infix, True))
# print(change_to_postfix(infix))
print(change_to_postfix(infix).items)
# print(calulate_infix(infix, True))
print(calulate_infix(infix))
# print(calulate_infix(infix, with_comma=True))
# print(add_comma(calulate_infix(infix)))
# print(remove_comma('123,000.000'))
# print("{:,}".format(calulate_infix(infix))) # old
# print(f"{calulate_infix(infix):,}") # >= python3.6

# print('postfix : ', change_to_postfix(infix, True))
# print('postfix : ', change_to_postfix(infix))
# print('result : ', calulate_infix(infix, True))
# print('result : ', calulate_infix(infix))
# """

# 15123.0 # 15,123.0
class Test13_comma(unittest.TestCase):
  def setUp(self) -> None:
    input1 = 15123
    output1 = '15,123'
    input2 = 15123.4567
    output2 = '15,123.4567'
    
    self.input1 = input1
    self.output1 = output1
    self.input2 = input2
    self.output2 = output2
    return super().setUp()
  
  def test_1(self):
    input1 = self.input1 
    output1 =self.output1
    input2 = self.input2 
    output2 =self.output2
    
    self.assertEqual(add_comma(input1), output1)
    self.assertEqual(add_comma(input2), output2)
    self.assertEqual(remove_comma(output1), input1)
    self.assertEqual(remove_comma(output2), input2)

# '12,000+3,123' # 15123.0
class Test12(unittest.TestCase):
  def setUp(self) -> None:
    infix = '12,000+3,123' # 15123.0
    postfix_result = '120003123+' # ['12000', '3123', '+']
    answer = 15123.0
    
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

# '(1234+2122)+33*432/532+(623*744-811)' # 12342122+33432*532/623744*811-++ # 466083.7969924812
class Test11(unittest.TestCase):
  def setUp(self) -> None:
    infix = '(1234+2122)+33*432/532+(623*744-811)' # 12342122+33432*532/623744*811-++ # 466083.7969924812
    postfix_result = '12342122+33432*532/623744*811-++' # ['1234', '2122', '+', '33', '432', '*', '532', '/', '623', '744', '*', '811', '-', '+', '+']
    answer = 466083.7969924812
    
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

# '(1234+2456)*323+71' # 12342456+323*71+ # 1191941.0
class Test10(unittest.TestCase):
  def setUp(self) -> None:
    infix = '(1234+2456)*323+71' # 12342456+323*71+ # 1191941.0
    postfix_result = '12342456+323*71+' # ['1234', '2456', '+', '323', '*', '71', '+']
    answer = 1191941.0
    
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

# '(12+245)*367' # 12245+367* # 94319
class Test9(unittest.TestCase):
  def setUp(self) -> None:
    infix = '(12+245)*367' # 12245+367* # 94319
    postfix_result = '12245+367*' # ['12', '245', '+', '367', '*']
    answer = 94319
    
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

# '(12*24)+35' = 323.0
class Test8(unittest.TestCase):
  def setUp(self) -> None:
    infix = '(12*24)+35' # 1224*35+ # 323.0
    postfix_result = '1224*35+' # ['12', '24', '*', '35', '+']
    answer = 323.0
    
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

# '12+3' = 15
class Test7(unittest.TestCase):
  def setUp(self) -> None:
    infix = '12+3' # 123+ # 15
    postfix_result = '123+' # ['12', '3', '+']
    answer = 15 
    
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

# """ unittest 코드 작동 일시 중지 
if __name__ == '__main__':
    unittest.main()
#  """