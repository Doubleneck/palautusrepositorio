import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        try:
            self.response = requests.get(url)
        except:
            print("Error, can´t access the given url")
    def get_players(self):
        players = []

        for player_dict in self.response.json():
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['games'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['assists'],
                player_dict['nationality'],
            )
            players.append(player)
        return players

    def get_request_time(self):
        return self.response.headers['Date']
