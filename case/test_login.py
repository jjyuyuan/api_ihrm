import json
import unittest

import requests
from parameterized import parameterized

import app
from api.login_api import LoginApi


def build_login_data():
    test_data = []
    with open(app.PRO_PATH + "/data/login_data.json", encoding="utf-8") as f:
        login_data = json.load(f)
        for item in login_data.values():
            test_data.append((item.get("mobile"),
                              item.get("password"),
                              item.get("success"),
                              item.get("code"),
                              item.get("message")))
    return test_data


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.login_api = LoginApi()

    def tearDown(self):
        self.session.close()

    @parameterized.expand(build_login_data())
    def test_login(self, mobile, password, success, code, message):
        response = self.login_api.login(self.session, mobile, password)
        self.assertEqual(success, response.json().get("success"))
        self.assertEqual(code, response.json().get("code"))
        self.assertIn(message, response.json().get("message"))

    def test_login_success(self):
        response = self.login_api.login(self.session, "13800000002", "123456")
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
        app.TOKEN = response.json().get("data")
