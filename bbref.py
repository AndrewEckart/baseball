import csv

def create_player_database(sourcepath='chadwick/people.csv'):
	player_database = open(sourcepath)
	player_reader = csv.DictReader(player_database)
	database = {}
	for row in player_reader:
		if row["mlb_played_last"]:
			if int(row["mlb_played_last"]) >= 2013:
				add_to_database(database,row)
		elif not row["mlb_played_first"] and row["pro_played_last"]:
			if int(row["pro_played_last"]) >= 2013:
				add_to_database(database,row)
	return database

def add_to_database(database,row):
	database[str(row["name_first"].replace(" ","")+" "+row["name_last"])] = row
#	if row["name_given"] != row["name_first"]:
#		database[str(row["name_given"]+" "+row["name_last"])] = row

def convert_player_bbref(playername,database):
	if playername not in database:
#		print("Player not found: ",playername)
		return None
	bbref_key = database[playername]["key_bbref"]
#	print("%s: %s" %(playername,bbref_key))
	return bbref_key

def convert_players(playerlist,database):
	missingcount = 0
	missing = []
	playerkeys = []
	for p in playerlist:
		p.brkey = convert_player_bbref(p.name,database)
		if p.brkey == None:
			missing.append(p.name)
			missingcount += 1
			continue
		playerkeys.append(p.brkey)
	print("Successfully converted %d players. %d players could not be found." %(len(playerkeys),missingcount))
	print("Missing players: ",missing)
	return playerkeys,missing