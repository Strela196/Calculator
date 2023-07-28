import unittest
from Reversepolishnotation import rpn
import sys
k = sys.stdin.readline()
o = sys.stdin.readline()
a = rpn(k)
b = rpn(o)
class test(unittest.TestCase):
    def test_isequal(self):
        if self.assertEqual(a , 11, "1 TEST FAILED"):
            print("")
        else:
            print("1 TEST PASSED")
        if self.assertEqual(b,  2.0, "2 TEST FAILED"):
            print("")
        else:
            print("2 TEST PASSED")
testing = test()
testing.test_isequal()