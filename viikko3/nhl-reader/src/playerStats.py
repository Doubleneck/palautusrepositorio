from player import Player

class PlayerStats:
    def __init__(self,reader):
        self.players = reader.get_players()
        self.time = reader.get_request_time()

    def top_scorers_by_nationality(self,nationality):
        
        players = []
        for player in self.players:
            if player.nationality == nationality:
                players.append(player)
        players.sort(key=lambda x: x.goals+x.assists, reverse=True)
        strPlayers = []
        for player in players:
            strPlayers.append(player.__str__())
       
        return strPlayers