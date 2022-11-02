import unittest
from statistics import Statistics
from player import Player
from enum import Enum

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]
class SortBy(Enum):
            POINTS = 1
            GOALS = 2
            ASSISTS = 3

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_testing_works(self):
        self.assertEqual(5, 5)    

    def test_search_finds_player(self):
        player = self.statistics.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")       

    def test_search_works_player_doesnt_exist(self):
        player = self.statistics.search("Nobody")
        self.assertEqual(player, None)

    def test_team_returns_right_players(self):
 
        players = self.statistics._players
        listEdmMembers= [players[0],players[2],players[4]]
        teamPlayers = self.statistics.team("EDM")
        self.assertEqual(listEdmMembers, teamPlayers)               

    def test_top_without_enum_returns_right_playerList(self):
 
        topPlayerS = self.statistics.top(2)
        listOfTwoFirstNames = [topPlayerS[0].name,topPlayerS[1].name]
        self.assertEqual(listOfTwoFirstNames,  ['Gretzky', 'Lemieux'])      

    def test_top_points_returns_right_playerList(self):
        topPlayerS = self.statistics.top(2,SortBy(SortBy.POINTS))
        listOfTwoFirstNames = [topPlayerS[0].name,topPlayerS[1].name]
        self.assertEqual(listOfTwoFirstNames,  ['Gretzky', 'Lemieux'])    

    def test_top_goals_returns_right_playerList(self):
        topPlayerS = self.statistics.top(2,SortBy.GOALS)
        listOfTwoFirstNames = [topPlayerS[0].name,topPlayerS[1].name]
        self.assertEqual(listOfTwoFirstNames,  ['Lemieux', 'Yzerman'])    

    def test_top_assists_returns_right_playerList(self):
        topPlayerS = self.statistics.top(2,SortBy.ASSISTS)
        listOfTwoFirstNames = [topPlayerS[0].name,topPlayerS[1].name]
        self.assertEqual(listOfTwoFirstNames,  ['Gretzky', 'Yzerman'])        

    


   
