import calendar
import datetime

import jwt

from constants import JWT_SECRET
from service.user import UserService


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def create_tokens(self, username, password, is_refresh=False):
        user = self.user_service.get_one_by_name(username)

        if user is None:
            raise Exception()

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                raise Exception()

        data = {
            'username': user.username,
            'role': user.role
        }

        min30 = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data['exp'] = calendar.timegm(min30.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm='HS256')
        days130 = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data['exp'] = calendar.timegm(days130.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm='HS256')
        return {"access_token": access_token, "refresh_token": refresh_token}

    def check_token(self, refresh_token):
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=['HS256'])
        username = data.get("username")

        user = self.user_service.get_one_by_name(username=username)
        if user is None:
            raise Exception()
        return self.create_tokens(username, user.password, is_refresh=True)
