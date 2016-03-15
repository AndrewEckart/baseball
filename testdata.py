import brscraper
import crawlplayer
import rosters
import players
import teams
import bbref
import openpyxl
import export

alex = players.Player('Alex','Rodriguez','NYY','Third Baseman')

alex.seasons = {
	"2015" : players.BatterSeason(alex,'NYY',2015,38,600,550,215,60,30,95,105,12),
	"2014" : players.BatterSeason(alex,'NYY',2014,37,600,550,214,60,25,90,120,12),
	"2013" : players.BatterSeason(alex,'NYY',2013,36,600,550,213,60,30,80,100,12),
	"1996" : players.BatterSeason(alex,'NYY',1996,19,600,550,196,60,28,95,105,12)
}

cc = players.Player('CC','Sabathia','NYY','Starting Pitcher')

cc.seasons = {
	"2015" : players.PitcherSeason(cc,'NYY',2015,34,33,33,18,9,221.1,0,190,60,150,68),
	"2012" : players.PitcherSeason(cc,'NYY',2012,34,33,33,20,9,231.1,0,190,60,150,78),
	"2008" : players.PitcherSeason(cc,'NYY',2008,34,33,33,18,7,226.2,0,190,60,150,80),
	"2005" : players.PitcherSeason(cc,'NYY',2005,34,33,33,18,13,201.0,0,190,60,150,90)
}

def test():
#	print(playerlist)
#	print(alex.displaySeasons())
#	print(cc.seasons)
	tj = players.Player('TJ','McFarland','BAL')
	tj.brkey = 'mcfartj01'
	tj.seasons = crawlplayer.get_all_seasons
	colby = players.Player('Colby','Lewis')
	colby.brkey = 'lewisco01'
	colby.seasons = crawlplayer.get_all_seasons(colby)
#	print(colby.seasons)
	ortega = players.Player('Rafael','Ortega')
	playerlist = [alex,cc,colby,ortega]
	export.export_data(playerlist,'testdata.xlsx',2015,3)

test()
