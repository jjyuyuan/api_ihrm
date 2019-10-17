import app


class UserApi:

    def add(self, session, username, mobile, workNumber):
        data = {
            "username": username,
            "mobile": mobile,
            "workNumber": workNumber
        }
        return session.post(app.BASE_URL + "/user", json=data, headers={"Authorization": "Bearer " + app.TOKEN})


    def update(self, session, username):
        data = {
            "username": username,
        }
        return session.put(app.BASE_URL + "/user/" + app.USER_ID, json=data, headers={"Authorization": "Bearer " + app.TOKEN})

    def get(self, session):
        return session.get(app.BASE_URL + "/user/" + app.USER_ID, headers={"Authorization": "Bearer " + app.TOKEN})

    def delete(self, session):
        return session.delete(app.BASE_URL + "/user/" + app.USER_ID, headers={"Authorization": "Bearer " + app.TOKEN})
