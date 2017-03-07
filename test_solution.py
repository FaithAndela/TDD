
import unittest
from tedd import solution
 class Test_Solution(unittest.TestCase):
  def test_addition(self):
    self.assertTrue(solution(10,20,"+"),30)

  def test_multiplication(self):
    self.assertTrue(solution(20,2,"*"),10)

  def test_Division(self):
    self.assertTrue(solution(20,2,"/"),10)


if __name__ == '__main__':
	unittest.main()