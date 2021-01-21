from flask_login import UserMixin
from .fix import getUser
class UserData:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        

class UserModel(UserMixin):
    def __init__(self, user_data):
        """
            param: user_data is class UserData
        """
        self.id = user_data.username
        self.password = user_data.password

    @staticmethod
    def query(user_id):
        user = getUser(user_id)
        user_data = UserData(
            username=user.username,
            password=user.password
        )

        return UserModel(user_data)
