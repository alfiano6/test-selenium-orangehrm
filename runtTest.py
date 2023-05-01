import unittest
from case import ADM

if __name__ == "__main__":
    suite = unittest.TestSuite()

    suite.addTest(ADM('ADM1'))
    suite.addTest(ADM('ADM2'))
    suite.addTest(ADM('ADM3'))
    suite.addTest(ADM('ADM4'))
    suite.addTest(ADM('ADM5'))
    suite.addTest(ADM('ADM6'))
    suite.addTest(ADM('ADM7'))
    suite.addTest(ADM('ADM8'))

runner = unittest.TextTestRunner()
runner.run(suite)