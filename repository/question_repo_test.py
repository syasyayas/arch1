import unittest
from model.question import Question
from question_repo import QuestionRepo


class TestQuestionRepo(unittest.TestCase):

    def test_add_question(self):
        question_repo = QuestionRepo()
        question = Question("2+2?", "4")
        question_repo.add_question(question)
        self.assertEqual(question_repo.questions[question.question], question)

    def test_add_question_empty_question(self):
        question_repo = QuestionRepo()
        empty_question = Question("", "")
        with self.assertRaises(Exception):
            question_repo.add_question(empty_question)

    def test_get_question_by_question(self):
        question_repo = QuestionRepo()
        question = Question("2+2=?", "4")
        question_repo.add_question(question)
        self.assertEqual(question_repo.get_question_by_question("2+2=?"), question)

    def test_get_question_by_question_not_found(self):
        question_repo = QuestionRepo()
        self.assertIsNone(question_repo.get_question_by_question("not exists"))

    def test_get_top_questions(self):
        question_repo = QuestionRepo()
        question1 = Question("Question 1", "1")
        question2 = Question("Question 2", "2")
        question3 = Question("Question 3", "3")

        question_repo.add_question(question1)
        question_repo.add_question(question2)
        question_repo.add_question(question3)

        question_repo.get_question_by_question(question1.question)
        question_repo.get_question_by_question(question1.question)

        question_repo.get_question_by_question(question2.question)
        question_repo.get_question_by_question(question2.question)
        question_repo.get_question_by_question(question2.question)
        question_repo.get_question_by_question(question2.question)

        top_questions = question_repo.get_top_questions(2)
        self.assertEqual(len(top_questions), 2)
        self.assertEqual(top_questions[0].get_id(), question2.get_id())
        self.assertEqual(top_questions[1].get_id(), question1.get_id())

    def test_get_top_questions_with_limit_zero(self):
        question_repo = QuestionRepo()
        with self.assertRaises(Exception):
            question_repo.get_top_questions(0)

    def test_get_top_questions_with_limit_greater_than_total_questions(self):
        question_repo = QuestionRepo()
        question1 = Question("Question 1", "1")
        question2 = Question("Question 2", "2")
        question_repo.add_question(question1)
        question_repo.add_question(question2)
        top_questions = question_repo.get_top_questions(3)
        self.assertEqual(len(top_questions), 2)
