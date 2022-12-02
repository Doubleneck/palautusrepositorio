from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, Or, Not, HasAtLeast, PlaysIn, All,  HasFewerThan

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    matcher = All()

    matcher = Not(
        #HasAtLeast(5, "goals"),
        #HasAtLeast(5, "assists"),
        PlaysIn("SEA")
    )
    matcher = And(
    HasFewerThan(1, "goals"),
    PlaysIn("NYR")
    )

    matcher = And(
    HasAtLeast(70, "points"),
    Or(
        PlaysIn("NYR"),
        PlaysIn("FLA"),
        PlaysIn("BOS")
    )
)
    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
