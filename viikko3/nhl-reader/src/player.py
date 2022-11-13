class Player:
    def __init__(self, name, team, games, goals, penalties, assists):
        self.name = name
        self.team = team
        self.games = games
        self.goals = goals
        self.penalties = penalties
        self.assists = assists

    
    def __str__(self):
        return (f"{self.name:20}" + ' goals ' +  str(self.goals) + ' + assists ' +  str(self.assists) + " = " + str(self.goals+self.assists))
