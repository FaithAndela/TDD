import unittest
from tdd import *
class Prime_Testcase(unittest.Test_Solution):
	def testif_prime(self):
		self.assertTrue(Solution(10),"is prime")

	def testif_prime(self):
		self.assertTrue(Solution(7),"Is prime")

	def testif_prime(self):
		self.assertTrue(Solution(5),"Not prime")

	def testif_prime(self):
		self.assertTrue(Solution(2),"Is prime")
		
	def testif_prime(self):
		self.assertNotIn(Solution(4),"Not prime")


