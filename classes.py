import json
import random


def load_data() -> dict:
    file = open("questions.json")
    loaded_data = json.load(file)
    return loaded_data


class Question:

    def __init__(self, question_text, question_level, correct_answer):

        self.question_text = question_text
        self.question_level = question_level
        self.correct_answer = correct_answer
        self.was_question_asked = False
        self.user_answer = None
        points_for_answer = 0
        if self.question_level == "1":
            points_for_answer = 10
        elif self.question_level == "2":
            points_for_answer = 20
        elif self.question_level == "3":
            points_for_answer = 30
        elif self.question_level == "4":
            points_for_answer = 40
        elif self.question_level == "5":
            points_for_answer = 50
        self.points_for_answer = points_for_answer


class Functions(Question):

    def is_correct(self):
        if self.correct_answer == self.user_answer:
            return True
        else:
            return False

    def build_question(self):
        print(f"Вопрос: {self.question_text}\nСложность {self.question_level}")

    def build_feedback(self):
        if self.is_correct():
            print(f" Ответ верный, получено {self.points_for_answer} баллов")
        else:
            print(f"Ответ неверный, верный ответ {self.correct_answer}")


def game_over(questions_list):
    print("Вот и всё!")
    print(f"Отвечено {len(questions_list) - questions_list.count(0)} вопроса из {len(questions_list)}")
    print(f"Набрано баллов {sum(questions_list)}")


def make_list():
    question_list = []
    for d in data_loaded:
        question_list.append(Functions(d["q"], d["d"], d["a"]))
        random.shuffle(question_list)
    return question_list


data_loaded = load_data()
questions = []

questions_orig = make_list()
for i in questions_orig:
    question1 = i
    question1.build_question()
    player_input = input()
    question1.user_answer = player_input
    if question1.is_correct():
        questions.append(question1.points_for_answer)
    else:
        questions.append(0)
    question1.build_feedback()

print(questions)
game_over(questions)
make_list()
