import unittest

import app
from case.test_login import TestLogin
from case.test_user import TestUser
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(TestLogin("test_login_success"))
suite.addTest(unittest.makeSuite(TestUser))
# runner = unittest.TextTestRunner()
# runner.run(suite)
with open(app.PRO_PATH + "/report/report.html", "wb") as f:
    runner = HTMLTestRunner(f, title="ihrm_report", description="ihrm_report")
    runner.run(suite)
