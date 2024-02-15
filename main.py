from model.user import User
from service.question_service import QuestionService


def print_hi(name):
    svc = QuestionService.new_service()

    user = svc.create_user()
    user2 = svc.create_user()

    svc.add_question("test1", "test")
    svc.add_question("test2", "test2")
    svc.add_question("test3", "test3")

    svc.find_answer_by_question("test", user.get_id())
    svc.find_answer_by_question("test1", user.get_id())
    svc.find_answer_by_question("test2", user.get_id())
    svc.find_answer_by_question("test3", user.get_id())
    svc.find_answer_by_question("test3", user.get_id())
    svc.find_answer_by_question("test3", user.get_id())
    svc.find_answer_by_question("test3", user.get_id())
    svc.find_answer_by_question("test3", user.get_id())
    svc.find_answer_by_question("test3", user.get_id())
    svc.find_answer_by_question("test3", user.get_id())
    svc.find_answer_by_question("test3", user.get_id())
    svc.find_answer_by_question("test3", user.get_id())
    svc.find_answer_by_question("test3", user.get_id())

    svc.find_answer_by_question("test", user2.get_id())
    svc.find_answer_by_question("test1", user2.get_id())
    svc.find_answer_by_question("test1", user2.get_id())
    svc.find_answer_by_question("test1", user2.get_id())
    svc.find_answer_by_question("test1", user2.get_id())
    svc.find_answer_by_question("test2", user2.get_id())

    print("########### TOP QUESTION ###########")
    svc.extract_top_questions()
    print("########### TOP QUESTION ###########")

    print()
    print()
    print()

    print("########### USERS ###########")
    svc.extract_users_with_questions()
    print("########### USERS ###########")


if __name__ == '__main__':
    print_hi('PyCharm')

