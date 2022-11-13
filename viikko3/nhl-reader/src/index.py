from playerReader import PlayerReader
from playerStats import PlayerStats
from player import Player

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    time = reader.get_request_time()
    nationality = "FIN"
    players = stats.top_scorers_by_nationality(nationality)
    print("Top Players from " + nationality + " " + time + "\n")
    for player in players:
        print(player)    

if __name__ == "__main__":
    main()
    