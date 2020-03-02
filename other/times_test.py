import unittest
from times import cps3037

class TestCPS3037(unittest.TestCase):
	def testCps3037(self):
		self.assertEqual(cps3037(4), 16)
