import brscraper
import unittest

## NOTE: If test module is located in 'unit-tests' child directory,
## it must be run from the application's root directory using "python -m unit-tests.testname"

class BRScraperFunctions(unittest.TestCase):
    
    def setUp(self):
        self.scraper = brscraper.BRScraper()
    
    def test_team(self):
        """Tests BRscraper on a team's franchise page."""
        resource = "teams/ARI/"
        data = self.scraper.parse_tables(resource)
        self.assertTrue("franchise_years" in data)
        for row in data["franchise_years"]:
            self.assertTrue("Year" in row)
            try: year = int(row["Year"])
            except: year = 0
            if year == 2011:
                self.assertTrue("W" in row)
                self.assertTrue(int(row["W"]) == 94)
            elif year == 2001:
                self.assertTrue("R" in row)
                self.assertTrue(int(row["R"]) == 818)

    def test_team_year(self):
        """Tests BRscraper on a team season page."""
        resource = "teams/ATL/1995.shtml"
        data = self.scraper.parse_tables(resource)
        self.assertTrue("team_pitching" in data)
        for row in data["team_pitching"]:
            self.assertTrue("Name" in row)
            if "Greg Maddux" in row["Name"]:
                self.assertTrue("BB") in row
                self.assertTrue(int(row["BB"]) == 23)
                self.assertTrue("SO") in row
                self.assertTrue(int(row["SO"]) == 181)
        self.assertTrue("team_batting" in data)
        for row in data["team_batting"]:
            self.assertTrue("Name" in row)
            if "Javy Lopez" in row["Name"]:
                self.assertTrue("BB") in row
                self.assertTrue(int(row["BB"]) == 14)
                self.assertTrue("SO") in row
                self.assertTrue(int(row["SO"]) == 57)
               
    def test_team_year_schedule(self):
        """Tests BRScraper on a team's season schedule page."""
        resource = "teams/BOS/2004-schedule-scores.shtml"
        data = self.scraper.parse_tables(resource)
        self.assertTrue("team_schedule" in data)
        for row in data["team_schedule"]:
            self.assertTrue("Gm#" in row)
            try: game = int(row["Gm#"])
            except: game = 0
            if game == 155:
                self.assertTrue("Opp" in row)
                self.assertTrue(row["Opp"] == "NYY")
                self.assertTrue("Win" in row)
                self.assertTrue(row["Win"] == "Schilling")
                self.assertTrue("Loss" in row)
                self.assertTrue(row["Loss"] == "Brown")
                self.assertTrue("Save" in row)
                self.assertTrue(row["Save"] == "")
    
    def test_player(self):
        """Tests BRscraper on a player page."""
        resource = "players/m/martipe02.shtml"
        data,role = self.scraper.parse_tables(resource,get_pos=True)
        self.assertTrue(role == "Pitcher")
        self.assertTrue("pitching_standard" in data)
        for row in data["pitching_standard"]:
            self.assertTrue("Year" in row)
            try: year = int(row["Year"])
            except: year = 0
            if year == 1999:
                self.assertTrue("HR" in row)
                self.assertTrue(int(row["HR"]) == 9)
                self.assertTrue("BF" in row)
                self.assertTrue(int(row["BF"]) == 835)
                self.assertTrue("W" in row)
                self.assertTrue(int(row["W"]) == 23)
        self.assertTrue("pitching_postseason" in data)
        for row in data["pitching_postseason"]:
            self.assertTrue("Year" in row)
            try: year = int(row["Year"])
            except: year = 0
            if year == 2004 and row["Series"] == "WS":
                self.assertTrue("SO" in row)
                self.assertTrue(int(row["SO"]) == 6)
    
    def test_manager(self):
        """Tests BRscraper on a manager page."""
        resource = "managers/aloufe01.shtml"
        data = self.scraper.parse_tables(resource)
        self.assertTrue("manager_stats" in data)
        for row in data["manager_stats"]:
            self.assertTrue("Year" in row)
            try: year = int(row["Year"])
            except: year = 0
            if year == 1992:
                self.assertTrue("W" in row)
                self.assertTrue(int(row["W"]) == 70)
            elif year == 2000:
                self.assertTrue("Tm" in row)
                self.assertTrue(row["Tm"] == "Montreal Expos")
    
    def test_mlb_year_standings(self):
        """Tests BRscraper on a league standings page."""
        resource = "leagues/MLB/1981-standings.shtml"
        data = self.scraper.parse_tables(resource)
        self.assertTrue("expanded_standings_overall" in data)
        for row in data["expanded_standings_overall"]:
            self.assertTrue("Tm" in row)
            if row["Tm"] == "OAK":
                self.assertTrue("L" in row)
                self.assertTrue(int(row["L"]) == 45)
            elif row["Tm"] == "SFG":
                self.assertTrue("Lg" in row)
                self.assertTrue(row["Lg"] == "NL")
    
    def test_awards_year(self):
        """Tests BRscraper on a season awards page."""
        resource = "awards/awards_1991.shtml"
        data = self.scraper.parse_tables(resource)
        self.assertTrue("AL_MVP_voting" in data)
        for row in data["AL_MVP_voting"]:
            self.assertTrue("Rank" in row)
            try: rank = int(row["Rank"])
            except: rank = 0
            if rank == 1:
                self.assertTrue("" in row)
                self.assertTrue("Tm" in row)
                self.assertTrue(row[""] == "Cal Ripken")
                self.assertTrue(row["Tm"] == "BAL")
    
                            
if __name__ == "__main__":
    unittest.main()
