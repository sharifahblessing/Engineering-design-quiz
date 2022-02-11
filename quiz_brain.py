import os
import random
from os import system, name


class QuizBrain:
    def __init__(self, quiz_questions, steps_examined_list):
        """ The initializer takes quiz_questions and steps_examined_list as a parameter
        The question_number, question_steps and step_id are set to start from zero"""
        self.question_number = 0
        self.question_list = quiz_questions
        self.questions_step = 0
        self.step_examined_list = steps_examined_list
        self.step_id = 0
        self.ref_id = None
        self.step_score = 0
        self.step_score_dict = {}
        self.player = None

    def next_question(self):
        """A method that picks a step dictionary of questions from the main question bank list and stores it in the
        current_question_step variable.
        The question_step_used variable stores a string of the  engineering step whose questions where picked.
        The strings are picked from the step_examined_list.
        The current_question_list variable stores a list value generated  from tapping into the steps
        dictionary questions stored in current_question_step with a key stored in question_step_used variable.
        The for loop repeats the code for generating questions within  it for the specified number
        of times in the range.
        """
        current_question_step = self.question_list[self.step_id]
        question_step_used = self.step_examined_list[self.step_id]
        current_question_list = current_question_step[question_step_used]
        for number_of_times in range(0, 2):
            self.print_question(current_question_list)
        self.update_step_score(update_score = self.step_score, engineering_step=question_step_used)
        self.reset_score()

    def set_player(self, player):
        self.player = player

    def print_question(self, current_question_list):
        """ It takes a current_question_list as an argument checks if the first generated index is not equal
        to the ref_id the question is generated.The generated question index is set as a reference_id else
         the function is recused to regenerate the indexes."""
        first_index_generated = random.randint(0, len(current_question_list) - 1)
        if first_index_generated != self.ref_id:
            current_question = current_question_list[first_index_generated]
            self.question_number += 1
            sep = " ,"
            user_answer = input(f"Q.{self.question_number} {current_question.qn_text} "
                                f"\n {current_question.qn_correct_answer}, "
                                f"{sep.join(current_question.qn_wrong_answer)}:")
            self.compare_answers(user_answer, current_question.qn_correct_answer)
            self.ref_id = first_index_generated
        else:
            self.print_question(current_question_list)

    def still_has_step(self):
        """Returns true or false if step_id is less or  greater than step_examined_list."""
        return self.step_id < len(self.step_examined_list)

    def next_step(self):
        """ This Increments the step_id"""
        self.step_id += 1

    def reset_quiz(self):
        """This sets the object to the initial set."""
        self.question_number = 0
        self.questions_step = 0
        self.step_id = 0

    def compare_answers(self, user_answer, question_correct_answer):
        """ Function compares answers entered by the user  with the question correct answer from the data file"""

        if user_answer.lower() == question_correct_answer.lower():
            self.step_score += 1
            print("You are right")
        else:
            print("You are wrong")
        print(f"Your current score is {self.step_score} ")
        print(f"The correct answer for this question is {question_correct_answer}")

    def update_step_score(self, update_score, engineering_step):
        self.player.update_student_score(engineering_step = engineering_step, score = update_score)
        # self.step_score_dict[engineering_step] = update_score
        # for step in self.step_examined_list:
        #     self.step_score_dict[step] = update_score
        print(f"Your current overall score for each step is {self.player.get_player_score()}")

    def displaying_step_score(self):
        for _ in self.step_examined_list:
            self.update_step_score(self.step_score, )
        print(self.step_score_dict)

    def reset_score(self):
        """This sets the object to the initial set."""
        self.step_score = 0





