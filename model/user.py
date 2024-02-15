import uuid

from model.question import Question


class User:
    __searched_questions: [Question]
    __id: uuid.uuid4

    def __init__(self):
        self.__searched_questions: [Question] = []
        self.__id = uuid.uuid4()

    def get_id(self) -> uuid.UUID:
        return self.__id

    def add_question(self, question: Question):
        if question not in self.__searched_questions:
            self.__searched_questions.append(question)

    def __str__(self):
        return f"ID: {self.__id}, Questions: [{'.'.join(map(str, self.__searched_questions))}]"

    def get_searched_questions(self) -> [Question]:
        return self.__searched_questions
