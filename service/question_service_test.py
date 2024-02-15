import unittest
import uuid
from model.question import Question
from model.user import User
from repository.question_repo import QuestionRepo
from repository.user_repo import UserRepo
from service.question_service import QuestionService


class TestQuestionService(unittest.TestCase):

    def setUp(self):
        self.question_service = QuestionService(QuestionRepo(), UserRepo())

    def test_add_question(self):
        question_text = "2+2"
        answer_text = "4"
        question = self.question_service.add_question(question_text, answer_text)

        self.assertIsInstance(question, Question)
        self.assertEqual(question.question, question_text)
        self.assertEqual(question.answer, answer_text)

    def test_get_answer_by_question_id(self):
        question_text = "2+2"
        answer_text = "4"
        added_question = self.question_service.add_question(question_text, answer_text)

        retrieved_answer = self.question_service.get_answer_by_question_id(question_text)
        self.assertEqual(retrieved_answer, answer_text)

    def test_find_answer_by_question(self):
        question_text = "2+2"
        answer_text = "5"
        added_question = self.question_service.add_question(question_text, answer_text)

        user = self.question_service.create_user()

        found_answer = self.question_service.find_answer_by_question(question_text, user.get_id())
        self.assertEqual(found_answer, answer_text)

        user = self.question_service.user_repo.get_user(user.get_id())
        self.assertEqual(len(user.get_searched_questions()), 1)

    def test_create_user(self):
        created_user = self.question_service.create_user()
        self.assertIsInstance(created_user, User)
