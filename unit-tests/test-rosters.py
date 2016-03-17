import brscraper
import rosters
import unittest
import teams
import players

## NOTE: If test module is located in 'unit-tests' child directory,
## it must be run from the application's root directory using "python -m unit-tests.testname"

class RosterFunctions(unittest.TestCase):
    
    def setUp(self):
        self.scraper = brscraper.BRScraper()
    
    def test_teamlist(self):
        """Test scraping of team abbreviations from a league's season page."""
        teamlist = rosters.get_teams(self.scraper,league='NL',year='2014')
        self.assertTrue('CIN' in teamlist)

    def test_team_roster(self):
        """Test scraping of a team's roster for a given season."""
        teamroster = rosters.get_team_roster(self.scraper,team='NYY',year='2014')
        self.assertTrue('Cesar Cabral' in teamroster)
        self.assertTrue(len(teamroster) == 58)

    def test_all_rosters(self):
        """Test scraping of all rosters given a list of teams."""
        teams = ['BAL','SEA']
        rosterlist,players = rosters.get_all_rosters(self.scraper,teams=teams,year='2013')
        self.assertTrue('SEA' in rosterlist)
        self.assertTrue('Felix Hernandez' in players)

    def test_create_rosters(self):
        """Test scraping of rosters for all teams given a league and season."""
        teamlist,playerlist = rosters.create_rosters(year='2012',league='AL')
        self.assertTrue(isinstance(teamlist[0],teams.Team))
        self.assertTrue(len(teamlist) == 15)
        self.assertTrue(isinstance(playerlist[0],players.Player))
        self.assertTrue(len(playerlist) == 704)
                    
if __name__ == "__main__":
    unittest.main()