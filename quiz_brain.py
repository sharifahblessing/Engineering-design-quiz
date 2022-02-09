import random


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

    def print_question(self, current_question_list):
        first_index_generated = random.randint(0, len(current_question_list) - 1)
        if first_index_generated != self.ref_id:
            current_question = current_question_list[first_index_generated]
            self.question_number += 1
            input(f"Q.{self.question_number} {current_question.qn_text}")
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





