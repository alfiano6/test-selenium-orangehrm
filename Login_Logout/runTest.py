import unittest
from case import TestLL

if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(TestLL('log1'))
    suite.addTest(TestLL('log2'))
    suite.addTest(TestLL('log3'))
    suite.addTest(TestLL('log4'))
    suite.addTest(TestLL('log5'))
    suite.addTest(TestLL('log6'))
    suite.addTest(TestLL('log7'))

runner = unittest.TextTestRunner()
runner.run(suite)