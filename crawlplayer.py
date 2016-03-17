import brscraper
import players

scraper = brscraper.BRScraper()

def get_player_page(player):
	player.url = "/players/%s/%s.shtml" %(player.brkey[0],player.brkey)
	playerpage,player.position = scraper.parse_tables(player.url,get_pos=True,std_only=True)
#	print("Player page downloaded.")
	return playerpage

def player_seasons(playerpage):
	playerseasons = {}
	for table in playerpage.keys():
		for row in playerpage[table]:
			if row['Year'] and row['Tm'] != 'Proj': #Ignore pre-season Marcel projections
				playerseasons[row['Year']] = row
	return playerseasons

def create_season(player,row):
	year = row['Year']
#	print("Creating %s season for %s from data: " %(year,player.name),row)
	if "Pitcher" not in player.position:
		age,pa,ab,hits,bb,hr,runs,rbi,sb = map(int,[row['Age'],row['PA'],row['AB'],row['H'],row['BB'],row['HR'],row['R'],row['RBI'],row['SB']])
		player.seasons[year] = players.BatterSeason(player,year,row['Tm'],age,pa,ab,hits,bb,hr,runs,rbi,sb)
	else:
		age,g,gs,w,l,sv,hits,bb,so,er = map(int,[row['Age'],row['G'],row['GS'],row['W'],row['L'],row['SV'],row['H'],row['BB'],row['SO'],row['ER']])
		ip = float(row['IP'])
		player.seasons[year] = players.PitcherSeason(player,year,row['Tm'],age,g,gs,w,l,ip,sv,hits,bb,so,er)

def get_all_seasons(player):
	player.seasons = {}
	player.page = get_player_page(player)
#	print(player.page)
	seasons = player_seasons(player.page)
#	print(seasons)
	for year in seasons.keys():
#		print(year)
		try: create_season(player,seasons[year])
		except: 
			print("%s season for %s could not be created from data: " %(year,player.name),seasons[year])
			continue
#		print(player.seasons[year])
	return player.seasons