import unittest
import uuid
from model.user import User
from model.question import Question
from user_repo import UserRepo


class TestUserRepo(unittest.TestCase):

    def test_add_user(self):
        user_repo = UserRepo()
        user = User()
        user_repo.add_user(user)
        self.assertEqual(user_repo.get_user(user.get_id()), user)

    def test_get_user_not_found(self):
        user_repo = UserRepo()
        non_existing_user_id = uuid.uuid4()
        with self.assertRaises(Exception):
            user_repo.get_user(non_existing_user_id)

    def test_update_user(self):
        user_repo = UserRepo()
        user = User()
        user_repo.add_user(user)

        user.add_question(Question("2+2=?", "4"))
        user_repo.update_user(user.get_id(), user)

        self.assertEqual(user_repo.get_user(user.get_id()), user)

    def test_add_user_searched_question(self):
        user_repo = UserRepo()
        user = User()
        question = Question("2+2=?", "4")
        user_repo.add_user(user)
        user_repo.add_user_searched_question(user.get_id(), question)

        updated_user = user_repo.get_user(user.get_id())
        self.assertTrue(question in updated_user.get_searched_questions())

    def test_get_all_users(self):
        user_repo = UserRepo()
        user1 = User()
        user2 = User()
        user_repo.add_user(user1)
        user_repo.add_user(user2)

        all_users = user_repo.get_all_users()
        self.assertEqual(len(all_users), 2)
