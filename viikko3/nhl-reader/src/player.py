class Player:
    def __init__(self, name, team, games, goals, penalties, assists):
        self.name = name
        self.team = team
        self.games = games
        self.goals = goals
        self.penalties = penalties
        self.assists = assists

    
    def __str__(self):
        return (
            self.name + ':' + ' team ' +  self.team + ' games '+ str(self.games)
            + ' goals ' +  str(self.goals) + ' penalties ' +  
            str(self.penalties)+ ' assists' +  str(self.assists))
