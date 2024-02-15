import typing

from model.question import Question


class QuestionRepo:
    def __init__(self):
        self.questions: typing.Dict[str, Question] = {}

    def add_question(self, question: Question):
        if question.question == "":
            raise Exception("Question should not be empty")
        if question.question in self.questions:
            return
        self.questions[question.question] = question

    def get_question_by_question(self, question: str) -> Question | None:
        if question not in self.questions:
            return None
        self.questions[question].usages = self.questions[question].usages + 1
        return self.questions[question]

    def get_top_questions(self, limit: int) -> typing.List[Question]:
        if limit <= 0:
            raise Exception("Limit should be greater than 0")
        if limit > len(self.questions):
            limit = len(self.questions)

        sorted_questions = sorted(self.questions.values(), key=lambda question: question.usages, reverse=True)
        return sorted_questions[:limit]
