import base64
import hashlib
import hmac

from constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        return self.dao.get_one(uid)

    def get_one_by_name(self, username):
        return self.dao.get_one_by_name(username)

    def get_all(self):
        return self.dao.get_all()

    def create(self, user_d):
        return self.dao.create(user_d)

    def delete(self, rid):
        self.dao.delete(rid)

    def update(self, user_d):
        self.dao.update(user_d)

    def make_user_password_hash(self, password):
        return base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        ))

    def compare_passwords(self, right_password_hash, user_pass):
        return hmac.compare_digest(
            base64.b64decode(right_password_hash),
            hashlib.pbkdf2_hmac('sha256', user_pass.encode('utf-8'), PWD_HASH_SALT, PWD_HASH_ITERATIONS))

