import unittest
import question2
class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(question2.smile(), ":)")
if __name__ == '__main__':
    unittest.main()
