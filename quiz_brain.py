import random


class QuizBrain:
    def __init__(self, quiz_questions, steps_examined_list):
        self.question_number = 0
        self.question_list = quiz_questions
        self.questions_step = 0
        self.step_examined_list = steps_examined_list
        self.step_id = 0

    def next_question(self):
        current_question_step = self.question_list[self.step_id]
        question_step_used = self.step_examined_list[self.step_id]
        current_question_list = current_question_step[question_step_used]
        for number_of_times in range(0, 2):
            index_generated = random.randint(0, len(current_question_list)-1)

            current_question = current_question_list[index_generated]
            input(f"{current_question.qn_text}")

    def still_has_step(self):
        return self.step_id < len(self.step_examined_list)

    def next_step(self):
        self.step_id += 1






