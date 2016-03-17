import crawlplayer
import rosters
import players
import teams
import bbref
import export
from tqdm import tqdm

def main(end=2015,numSeasons=3,exportplayers=False,destpath='brdata.xlsx'):
	teamlist,playerlist = rosters.create_rosters()
	crawl_players(playerlist)
	export.export_data(playerlist,destpath,end,numSeasons)
	return

def crawl_players(playerlist):
	chadwick = bbref.create_player_database()
	print("Chadwick database successfully initialized: %d records." %len(chadwick))
	playerkeys,missing = bbref.convert_players(playerlist,chadwick)
	print("Crawling player pages ...")
	for p in tqdm(playerlist):
		if p.brkey:
			p.seasons = crawlplayer.get_all_seasons(p)
	return playerkeys

def sort_players(playerlist):
	hitterlist,pitcherlist = [],[]
	for player in playerlist:
		if "Pitcher" in player.position:
			pitcherlist.append(player)
		else:
			hitterlist.append(player)
	return hitterlist,pitcherlist

main()