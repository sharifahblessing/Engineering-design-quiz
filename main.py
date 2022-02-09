
from data import question_data
from turtle import Screen
from question import Question
from quiz_brain import QuizBrain


# Todo Utilise turtle graphics module : screen input title(Engineering design steps Yiya game) prompt"Welcome to the
#  user game how many users do we have?
#  store the number of users in a variable.

screen = Screen()
screen.screensize(canvwidth = 800, canvheight = 800)
number_of_players = screen.textinput(title = "Engineering design quiz", prompt = "How many players do we have?")
screen.title("Engineering design game")

print(f"Welcome to the Yiya Engineering design quiz, We have {number_of_players} players ")

# Prompting the named number of players to enter there names
players = []
for player_index in range(int(number_of_players)):
    player_index += 1
    name_of_player = input(f"Player number {player_index} please register your name? ")
    players.append(name_of_player)

print(f"{','.join(players)},Please get ready to answer the quiz! ")

# Todo.  Have a data file with a dictionary  with engineering design steps as keys and a dictionary of
#  dictionaries of questions  as the values.The questions dictionary consist of question text, correct answer
#  and other answers as values.
steps_examined = []

main_question_bank = []
# Todo Access the question_information by looping through question_data dictionary in the data file
for step in question_data:
    steps_examined.append(step)
    step_questions_list = question_data[step]
    step_question_bank = []
    # Todo Generate a question objects from the question blue print and add them to the step question bank
    for question_information in step_questions_list:

        new_question = Question(text = question_information["question_text"],
                                correct_answer = question_information["correct_answer"],
                                wrong_answer = question_information["wrong_answers"])
        step_question_bank.append(new_question)
    # Todo Formulate a dictionary that will have the step as a key and the generated question_bank list as a value
    step_question_bank_dictionary = {step: step_question_bank}
    # Todo Append the generated step_question_bank_dictionaries in the main question_bank list.
    main_question_bank.append(step_question_bank_dictionary)
# print(main_question_bank)

quiz = QuizBrain(quiz_questions = main_question_bank, steps_examined_list = steps_examined)

quiz_is_on = True


while quiz_is_on:
    for player_index in range(int(number_of_players)):
        print(f'{players[player_index]}, it is your turn')
        while quiz.still_has_step():
            quiz.next_question()
            quiz.next_step()
        if player_index != int(number_of_players)-1:
            quiz.reset_quiz()
        print(f'Thank you, {players[player_index]}')
    quiz_is_on = False


# Todo The question bank that will be used in the question,
#  that will contain two randomly generated questions
#  from each step for each player

#
#  Todo Let the number of users  stored on the above variable enter there names .
#   users names entered formulate keys, there score are values,update user scores.
#  Todo formulate an empty dictionary. that will have

# player_score_log = []
# # player_grades ={}
# # player_grades[player] = {}
# step1_score = 0
# step2_score = 0
# step3_score = 0
# total_score = 0

# for player in players:
#     player_data = {"player": player,
#                    "step1_score": step1_score,
#                    "step2_score": step2_score,
#                    "step3_score": step3_score,
#                    "total_score": total_score}
#     player_score_log.append(player_data)
# print(player_score_log)
#
# #  Todo In turns invite the registered users to answer the questions
# #      Generate user questions randomly from the different design steps
# #      Give them two chances if they answer incorrectly
# #      Declare the winner with the step with passed most.
#
#
# def generate_player(players_list):
#
#     new_player = players_list[random.randint(0, len(players_list))]
#     return new_player


# game_is_on = True
# while game_is_on:
#     for player in players:
#         print(f"{player} your questions are? ")
#         for index in range(0, len(players)):
#             question_1 = question_bank[index]
#             user_answer = input(f"{question_1['question_text']}\n {', '.join({question_1['correct_answer']})} "
#                                 f" {question_1['wrong_answers']}")
#             if user_answer.lower() == question_1['correct_answer'].lower():
#                 print("Hello world")
#             else:
#                 game_is_on = False


# display winner on scoreboard
