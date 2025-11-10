import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
	
	# Tarkistetaan löytyykö pelaajaa valitulla nimellä
    def test_search_oikea_pelaaja(self):
        player = self.stats.search("Gretzky")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Gretzky")
        self.assertEqual(player.team, "EDM")

	# Tarkistetaan tuntemattomalla nimellä haku
    def test_search_ei_pelaajaa(self):
        player = self.stats.search("McDavid")
        self.assertIsNone(player)

	# Tarkistetaan joukkueen pelaajat
    def test_team_joukkueen_pelaajat(self):
        edm_players = self.stats.team("EDM")
        self.assertEqual(len(edm_players), 3)
        names = [p.name for p in edm_players]
        self.assertIn("Kurri", names)
        self.assertIn("Gretzky", names)
        self.assertIn("Semenko", names)
	
	# Testataan parhaiden pelaajien oikea pyydetty määrä (+1 koska while <=)
    def test_top_oikea_maara(self):
        top_players = self.stats.top(2)
        self.assertEqual(len(top_players), 3)
	
	# Tarkistetaan parhaiden pelaajien järjestys
    def test_top_oikea_jarjestys(self):
        top_players = self.stats.top(1)
        self.assertEqual(top_players[0].name, "Gretzky")