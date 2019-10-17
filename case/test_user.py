import unittest
import requests

import app
from api.user_api import UserApi


class TestUser(unittest.TestCase):

    def setUp(self):
        self.session = requests.Session()
        self.user_api = UserApi()

    def tearDown(self):
        self.session.close()

    def test_1_add(self):
        response = self.user_api.add(self.session, "tom", "13900000039", "13900000039")
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))
        app.USER_ID = response.json().get("data").get("id")

    def test_2_update(self):
        response = self.user_api.update(self.session, "tom_new")
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    def test_3_get(self):
        response = self.user_api.get(self.session)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))

    def test_4_delete(self):
        response = self.user_api.delete(self.session)
        self.assertEqual(True, response.json().get("success"))
        self.assertEqual(10000, response.json().get("code"))
        self.assertIn("操作成功", response.json().get("message"))


