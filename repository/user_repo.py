import typing
import uuid

from model.question import Question
from model.user import User


class UserRepo:
    def __init__(self):
        self.__users: typing.Dict[uuid.UUID, User] = {}

    def add_user(self, user: User) -> None:
        self.__users[user.get_id()] = user

    def get_user(self, user_id: uuid.UUID) -> User:
        if user_id not in self.__users:
            raise Exception("User not found")
        return self.__users.get(user_id)

    def update_user(self, user_id: uuid.UUID, user: User) -> None:
        if user_id not in self.__users:
            raise Exception("User not found")
        self.__users[user.get_id()] = user

    def add_user_searched_question(self, user_id: uuid.UUID,question: Question) -> None:
        user = self.get_user(user_id)
        user.add_question(question)
        self.update_user(user_id, user)

    def get_all_users(self) -> typing.List[User]:
        return list(self.__users.values())