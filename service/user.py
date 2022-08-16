from dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, uid):
        pass

    def get_one_by_name(self, username):
        pass

    def get_all(self):
        pass

    def create(self, user_d):
        pass

    def delete(self, rid):
        pass

    def update(self, user_d):
        pass

    def make_user_password_hash(self, password):
        pass

    def compare_passwords(self, pass_hash, user_pass):
        pass
