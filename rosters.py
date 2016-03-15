import brscraper
import openpyxl
import csv
import teams
import players

scraper = brscraper.BRScraper()

def get_teams(scraper,league='AL',year="2015"):
	teams = []
	leagueurl = "leagues/%s/%s.shtml" %(league,year)
	leaguepage = scraper.parse_tables(leagueurl)[0]
	for tm in leaguepage["teams_standard_batting"]:
		teams.append(tm["Tm"])
	return teams

def get_team_roster(scraper,team,year="2015"):
	teamroster = []
	teamurl = "teams/%s/%s-roster.shtml" %(team,year)
	teampage = scraper.parse_tables(teamurl)[0]
	for player in teampage["40man"]:
		teamroster.append(player["Name"])
	return teamroster

def get_all_rosters(scraper,teams):
	rosters = {}
	players = []
	for tm in teams:
		rosters[tm] = get_team_roster(scraper,tm)
		players = players + rosters[tm]
#	save_players(players)
	return rosters,players

def save_players(playerlist,outfile="players.csv"):
	out = open(outfile, 'w')
	for p in playerlist:
		out.write('%s,\n' %p)
	out.close()

def create_rosters(year=2015):
	print("Building rosters ...")
	teamabbs = get_teams(scraper)
	print("Rosters will be generated for the following teams: ",teamabbs)
	teamlist,playerlist = [],[]
	for tm in teamabbs:
		roster = get_team_roster(scraper,tm,year)
		teamlist.append(teams.Team(tm,year,roster))
#		print("%s roster: %d players." %(tm,len(roster)))
		for player in roster:
			firstname,lastname = player.split(' ',1)
			playerlist.append(players.Player(firstname,lastname,tm))
	print("Roster generation complete. Team and Player objects created.")
	return teamlist,playerlist