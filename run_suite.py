import unittest

from case.test_login import TestLogin
from case.test_user import TestUser

suite = unittest.TestSuite()
suite.addTest(TestLogin("test_login_success"))
suite.addTest(unittest.makeSuite(TestUser))
runner = unittest.TextTestRunner()
runner.run(suite)
