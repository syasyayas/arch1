import uuid
from uuid import UUID


class Question:
    question: str
    answer: str
    usages: int
    __id: uuid.uuid4

    def __init__(self, question: str, answer: str) -> None:
        self.question = question
        self.answer = answer
        self.usages = 0
        self.__id = uuid.uuid4()

    def __str__(self) -> str:
        return f"Question: {self.question} Answer: {self.answer} Usages: {self.usages} "

    def get_id(self) -> UUID:
        return self.__id
