class Player:
    def __init__(self, player_name, examined_step_list):
        self.user_name = player_name
        self.player_score = {}
        self.step_list = examined_step_list
        self.generate_score_dict()

    def generate_score_dict(self):
        for key in self.step_list:
            self.player_score[key] = 0

    def update_student_score(self, engineering_step, score):
        self.player_score[engineering_step] = score

    def get_player_name(self):
        return self.user_name

    def get_player_score(self):
        return self.player_score


