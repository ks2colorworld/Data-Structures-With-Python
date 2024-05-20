import unittest
from calculator import add_comma, change_to_postfix,calculate_postfix,calculate_infix, remove_comma

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
# infix = '12,000+3,123' # 15,123.0
# infix = '12,000,000+3,123' # 

# infix = '2/3' 
# (){}[] 괄호 대응 
# infix = '{12+245}*367' # 12245+367* # 94319
# infix = "{[1000 + 2,000] * 4 - (4 / 2)}" # 10002000+4*42/- # 11998.0
# infix = "{[1000 + 2,000] * 4 - (4 / 2)})" # error 

# infix = '100+-50'
# infix = '100--50'
# infix = '(-100+50)*-10'
# infix = '(-100+50)-10'
infix = "{[1000 + -2,000] * 4 - (4 / 2)}"  

print('infix : ', infix)
# print(change_to_postfix(infix, True))
print('postfix : ', change_to_postfix(infix))
print('postfix : ', change_to_postfix(infix).items)
# print(calculate_infix(infix, True))
print('result : ', calculate_infix(infix))
# print('result : ', calculate_infix(infix, with_comma=True))
# print(add_comma(calculate_infix(infix)))
# print(remove_comma('123,000.000'))
# print("{:,}".format(calculate_infix(infix))) # old
# print(f"{calculate_infix(infix):,}") # >= python3.6

# print('postfix : ', change_to_postfix(infix, True))
# print('postfix : ', change_to_postfix(infix))
# print('result : ', calculate_infix(infix, True))
# print('result : ', calculate_infix(infix))
# """

# "{[1000 + 2,000] * 4 - (4 / 2)})" # error : brackets are mismatched
class Test16_ErrorCheck(unittest.TestCase):
  def setUp(self) -> None:
    input1 = "{[1000 + 2,000] * 4 - (4 / 2)})" # error 
    
    self.input1 = input1
    return super().setUp()
  
  def test_match_brackets_fail(self):
    input1 = self.input1
    # ValueError가 발생하는지 테스트
    with self.assertRaises(ValueError) as context:
      calculate_infix(input1)
    
    self.assertEqual(str(context.exception), "brackets are mismatched")

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

# 음수(-) 대응 테스트
class Test17(unittest.TestCase):
  def test_1(self):
    infix1 = '100+-50'
    infix2 = '100--50'
    infix3 = '(-100+50)*-10'
    infix4 = '(-100+50)-10'
    infix5 = "{[1000 + -2,000] * 4 - (4 / 2)}"  
    
    postfix_result1 = '100-50+' # ['100', '-50', '+']
    postfix_result2 = '100-50-' # ['100', '-50', '-']
    postfix_result3 = '-10050+-10*' # ['-100', '50', '+', '-10', '*']
    postfix_result4 = '-10050+10-' # ['-100', '50', '+', '10', '-']
    postfix_result5 = '1000-2000+4*42/-' # ['1000', '-2000', '+', '4', '*', '4', '2', '/', '-']

    answer1 = 50.0
    answer2 = 150.0
    answer3 = 500.0
    answer4 = -60.0
    answer5 = -4002.0
    
    postfix1 = change_to_postfix(infix1, False) # stack
    postfix2 = change_to_postfix(infix2, False) # stack
    postfix3 = change_to_postfix(infix3, False) # stack
    postfix4 = change_to_postfix(infix4, False) # stack
    postfix5 = change_to_postfix(infix5, False) # stack
    
    # print('postfix : ', change_to_postfix(infix1, False))
    self.assertEqual(''.join(map(str, postfix1)), postfix_result1)
    self.assertEqual(''.join(map(str, postfix2)), postfix_result2)
    self.assertEqual(''.join(map(str, postfix3)), postfix_result3)
    self.assertEqual(''.join(map(str, postfix4)), postfix_result4)
    self.assertEqual(''.join(map(str, postfix5)), postfix_result5)
    
    # print('result : ', calculate_infix(infix1, False))
    # self.assertEqual(calculate_infix(infix1, False), answer1)
    self.assertEqual(calculate_postfix(postfix1, False), answer1)
    self.assertEqual(calculate_postfix(postfix2, False), answer2)
    self.assertEqual(calculate_postfix(postfix3, False), answer3)
    self.assertEqual(calculate_postfix(postfix4, False), answer4)
    self.assertEqual(calculate_postfix(postfix5, False), answer5)

# "{[1000 + 2,000] * 4 - (4 / 2)}" # 10002000+4*42/- # 11998.0
class Test15(unittest.TestCase):
  def setUp(self) -> None:
    infix = "{[1000 + 2,000] * 4 - (4 / 2)}" # 10002000+4*42/- # 11998.0
    postfix_result = '10002000+4*42/-' # ['1000', '2000', '+', '4', '*', '4', '2', '/', '-']
    answer = 11998.0
    
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

# '{12+245}*367' # 12245+367* # 94319
class Test14(unittest.TestCase):
  def setUp(self) -> None:
    infix = '{12+245}*367' # 12245+367* # 94319.0
    postfix_result = '12245+367*' # ['12', '245', '+', '367', '*']
    answer = 94319.0
    
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