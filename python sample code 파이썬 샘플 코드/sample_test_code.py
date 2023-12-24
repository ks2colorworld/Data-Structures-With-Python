import unittest

# 테스트할 함수 또는 클래스 정의
def add(a, b):
    return a + b

class TestAddFunction(unittest.TestCase):

    # 각 테스트 케이스는 'test_'로 시작해야 함
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_add_mixed_numbers(self):
        self.assertEqual(add(2, -3), -1)

# 스크립트가 메인으로 실행될 때 unittest 테스트 실행
if __name__ == '__main__':
    unittest.main()
