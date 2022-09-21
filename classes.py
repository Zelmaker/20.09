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
        self.points_for_answer = self.get_points()

    def get_points(self):
        return int(self.question_level) * 4

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


def game_over(sum_of_points):
    print("Вот и всё!")
    print(f"Отвечено {len(sum_of_points) - sum_of_points.count(0)} вопроса из {len(sum_of_points)}")
    print(f"Набрано баллов {sum(sum_of_points)}")


def make_list():
    question_list = []
    for d in data_loaded:
        question_list.append(Question(d["q"], d["d"], d["a"]))
        random.shuffle(question_list)
    return question_list


data_loaded = load_data()
sum_of_points = []
questions_orig = make_list()

for i in questions_orig:
    i.build_question()
    player_input = input()
    i.user_answer = player_input
    if i.is_correct():
        sum_of_points.append(i.points_for_answer)
    else:
        sum_of_points.append(0)
    i.build_feedback()
game_over(sum_of_points)
make_list()
