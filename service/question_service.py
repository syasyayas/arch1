import uuid

from model.question import Question
from model.user import User
from repository.question_repo import QuestionRepo
from repository.user_repo import UserRepo


class QuestionService:

    def __init__(self, question_repo: QuestionRepo, user_repo: UserRepo):
        self.question_repo = question_repo
        self.user_repo = user_repo

    @classmethod
    def new_service(cls):
        return QuestionService(QuestionRepo(), UserRepo())

    def add_question(self, question: str, answer: str) -> Question:
        question = Question(question=question, answer=answer)
        self.question_repo.add_question(question)
        return question

    def get_answer_by_question_id(self, question: str) -> str:
        question = self.question_repo.get_question_by_question(question)
        if question is None:
            return ""
        return question.answer

    def find_answer_by_question(self, question: str, user_id: uuid.UUID) -> str | None:

        found_question = self.question_repo.get_question_by_question(question)
        if found_question is None:
            return None

        self.user_repo.add_user_searched_question(user_id, found_question)

        return found_question.answer

    def extract_top_questions(self) -> None:
        top_questions = self.question_repo.get_top_questions(10)
        print("\n".join(map(str, top_questions)))

    def extract_users_with_questions(self) -> None:
        users = self.user_repo.get_all_users()
        print("\n".join(map(str, users)))

    def create_user(self) -> User:
        user = User()
        self.user_repo.add_user(user)
        return user