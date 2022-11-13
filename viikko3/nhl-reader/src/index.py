import requests
from player import Player


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    response = requests.get(url).json()
    headers = requests.get(url).headers['Date']
    nationality = 'FIN'
    print("Players from " + nationality + " " +headers + "\n")

    players = []

    for player_dict in response:
        if player_dict['nationality'] == nationality:
            player = Player(
                player_dict['name'],
                player_dict['team'],
                player_dict['games'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['assists'],
            )
            players.append(player)
    for player in players:
        print(player) 

if __name__ == "__main__":
    main()
    
