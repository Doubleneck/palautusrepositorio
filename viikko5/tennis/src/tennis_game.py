class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_score += 1
        else:
            self.player2_score += 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.get_score_if_draw_and_both_scores_under_4()

        elif self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_score_if_player1_or_player2_score_is_4_or_more()

        else:
            return self.get_score_if_not_draw_and_both_scores_under_4()

    def get_score_if_draw_and_both_scores_under_4(self):
        if self.player1_score == 0:
            score_description = "Love-All"
        elif self.player1_score == 1:
            score_description = "Fifteen-All"
        elif self.player1_score == 2:
            score_description = "Thirty-All"
        elif self.player1_score == 3:
            score_description = "Forty-All"
        else:
            score_description = "Deuce"
        return score_description

    def get_score_if_player1_or_player2_score_is_4_or_more(self):
        if self.player1_score - self.player2_score == 1:
            score_description = "Advantage player1"
        elif self.player1_score - self.player2_score == -1:
            score_description = "Advantage player2"
        elif self.player1_score - self.player2_score >= 2:
            score_description = "Win for player1"
        else:
            score_description = "Win for player2"
        return score_description

    def get_score_if_not_draw_and_both_scores_under_4(self):
        if self.player1_score == 0:
            player1_score_description = "Love-"
        elif self.player1_score == 1:
            player1_score_description = "Fifteen-"
        elif self.player1_score == 2:
            player1_score_description = "Thirty-"
        elif self.player1_score == 3:
            player1_score_description = "Forty-"

        if self.player2_score == 0:
            player2_score_description = "Love"
        elif self.player2_score == 1:
            player2_score_description = "Fifteen"
        elif self.player2_score == 2:
            player2_score_description = "Thirty"
        elif self.player2_score == 3:
            player2_score_description = "Forty"

        return player1_score_description + player2_score_description
