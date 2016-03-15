import brscraper

scraper = brscraper.BRScraper()

def get_teams(scraper,league='AL',year="2015"):
	teams = []
	leagueurl = "leagues/%s/%s.shtml" %(league,year)
	leaguepage = scraper.parse_tables(leagueurl)
	for tm in leaguepage["teams_standard_batting"]:
		teams.append(tm["Tm"])
	print(teams)
	return teams

def get_team_roster(scraper,team,year="2015"):
	teamroster = []
	teamurl = "teams/%s/%s-roster.shtml" %(team,year)
	teampage = scraper.parse_tables(teamurl)
	for player in teampage["40man"]:
		teamroster.append(player["Name"])
	return teamroster

teams = get_teams(scraper)
print(get_team_roster(scraper,'NYY'))

#result = scraper.parse_tables("teams/NYY/2016.shtml")
#print(vars(scraper))
#print(result)