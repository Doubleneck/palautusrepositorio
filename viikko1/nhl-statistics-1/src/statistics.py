from player_reader import PlayerReader


def sort_by_points(player):
    return player.points

def sort_by_goals(player):
    return player.goals

def sort_by_assists(player):
    return player.assists
   

class Statistics:
    def __init__(self,playerreader):
        self.reader = playerreader
        self._players = self.reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, enum = 1):
        if enum == 1:
            sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        )
        elif enum.value == 1:
            sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_points
        ) 
        elif enum.value == 2:
            sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_goals
        ) 
        else:
            sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by_assists
        ) 
        
        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result 
