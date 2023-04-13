from parameterized import parameterized, parameterized_class
import unittest
from clase11_4 import fibonacci
class Mytest(unittest.TestCase):
    @parameterized.expand([
        (1,1),
        (2,1),
        (3,2),
        (4,3),
        (5,5),
        (6,8),
        
    ])
    def test(self, num, res):
        self.assertEqual(fibonacci(num),res)

if __name__ == '__main__':
    unittest.main()