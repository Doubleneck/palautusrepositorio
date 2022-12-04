from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, Or, Not, HasAtLeast, PlaysIn, All,  HasFewerThan

class Build:
    def __init__(self):
        self.alkiot = []

    def push(self, alkio):
        self.alkiot.append(alkio)

    def pop(self):
        return self.alkiot.pop()

    def empty(self):
        return len(self.alkiot) == 0
        

class Querybuilder:
    def __init__(self, build = Build()):
        self.build_olio = build
        
        if not type(self.build_olio) is type(And()):
            self.build_olio = All()
    
    def playsIn(self, team):   
        return Querybuilder(And(self.build_olio,PlaysIn(team)))
    
    def hasAtLeast(self, points, attr):
        return Querybuilder(And(self.build_olio,HasAtLeast(points,attr)))

    def hasFewerThan(self, points, attr):
        return Querybuilder(And(self.build_olio,HasFewerThan(points,attr)))

    def build(self):
        return self.build_olio

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
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
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

    query = Querybuilder()
    matcher = query.build()
    matcher = query.hasAtLeast(10, "goals").hasFewerThan(20, "goals").playsIn("NYR").build()

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
