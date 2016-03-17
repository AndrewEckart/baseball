import brscraper
import openpyxl
import csv
import teams
import players
from tqdm import tqdm

scraper = brscraper.BRScraper()

def get_teams(scraper,league='AL',year='2015'):
	teams,leagueurl = [],('leagues/%s/%s.shtml' %(league,year))
	leaguepage = scraper.parse_tables(leagueurl)
	for tm in leaguepage['teams_standard_batting']: teams.append(tm['Tm'])
	return teams

def get_team_roster(scraper,team,year='2015'):
	teamroster,teamurl = [],('teams/%s/%s-roster.shtml' %(team,year))
	teampage = scraper.parse_tables(teamurl)
	if '40man' in teampage.keys(): table = '40man'
	elif 'appearances' in teampage.keys(): table = 'appearances'
	else:
		print("No roster table could be found on page: %s" %teamurl)
		return []
	for player in teampage[table]:
		teamroster.append(player['Name'])
	return teamroster

def get_all_rosters(scraper,teams,year='2015'):
	rosters = {}
	players = []
	for tm in teams:
		rosters[tm] = get_team_roster(scraper,tm)
		players = players + rosters[tm]
	return rosters,players

def export_playerlist(playerlist,destpath='playerlist.csv'):
	with open(destpath, 'w') as out:
		for p in playerlist:
			out.write('%s,\n' %p)

def create_rosters(year=2015,league='AL',export=False,destpath='playerlist.csv'):
	print("Building rosters ...")
	teamabbs = get_teams(scraper,league=league)
	print("Rosters will be generated for the following teams: ",teamabbs)
	teamlist,playerlist = [],[]
	for tm in tqdm(teamabbs):
		roster = get_team_roster(scraper,tm,year)
		teamlist.append(teams.Team(tm,year,roster))
#		print("%s roster: %d players." %(tm,len(roster)))
		for player in roster:
			firstname,lastname = player.split(' ',1)
			playerlist.append(players.Player(firstname,lastname,tm))
	print("Roster generation complete. Team and Player objects created.")
	if export:
		print("Exporting results to %s." %destpath)
		export_playerlist(playerlist,destpath=destpath)
	return teamlist,playerlist