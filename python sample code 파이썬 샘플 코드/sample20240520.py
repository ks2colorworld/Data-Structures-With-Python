def checkTrue(value_bool:bool):
  if value_bool:
    return value_bool
  else:
    raise ValueError(f"value_bool is false")
  

# print(checkTrue(True)) # True
# print(checkTrue(False)) # Error


import unittest

class TestCheckTrue(unittest.TestCase):
    
    def test_check_true_with_true(self):
        # True 값을 전달했을 때 올바른 값을 반환하는지 테스트
        self.assertTrue(checkTrue(True))
    
    def test_check_true_with_false(self):
        # False 값을 전달했을 때 ValueError가 발생하는지 테스트
        with self.assertRaises(ValueError) as context:
            checkTrue(False)
        
        self.assertEqual(str(context.exception), "value_bool is false")

# unittest.main()은 스크립트가 직접 실행될 때만 호출되며
# 테스트 케이스를 실행합니다.
if __name__ == '__main__':
    unittest.main()
