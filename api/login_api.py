import app


class LoginApi:

    def login(self, session, mobile, password):
        data = {
            "mobile": mobile,
            "password": password
        }
        return session.post(app.BASE_URL + "/login", json=data)
