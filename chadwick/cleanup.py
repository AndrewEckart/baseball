import csv

sourcepath = 'people_all.csv'
outpath = 'people.csv'

player_database = open(sourcepath)
player_reader = csv.DictReader(player_database)

print("Imported data from file: ",sourcepath)

database = {}
for row in player_reader:
		if row["mlb_played_last"]:
			if int(row["mlb_played_last"]) >= 2013:
				database[str(row["name_first"]+" "+row["name_last"])] = row
		elif not row["mlb_played_first"] and row["pro_played_last"]:
			if int(row["pro_played_last"]) >= 2014:
				database[str(row["name_first"]+" "+row["name_last"])] = row	

print(len(database)," valid records found.")
#print(database["Alex Rodriguez"])

print("Exporting data to file: ",outpath)
outfile = open(outpath, 'w')
fields = "key_person,key_uuid,key_mlbam,key_retro,key_bbref,key_bbref_minors,key_fangraphs,key_npb,key_sr_nfl,key_sr_nba,key_sr_nhl,key_findagrave,name_last,name_first,name_given,name_suffix,name_matrilineal,name_nick,birth_year,birth_month,birth_day,death_year,death_month,death_day,pro_played_first,pro_played_last,mlb_played_first,mlb_played_last,col_played_first,col_played_last,pro_managed_first,pro_managed_last,mlb_managed_first,mlb_managed_last,col_managed_first,col_managed_last,pro_umpired_first,pro_umpired_last,mlb_umpired_first,mlb_umpired_last"
fieldnames = fields.split(",")
#print("Fields: ",fieldnames)
writer = csv.DictWriter(outfile,fieldnames,lineterminator='\n')

writer.writeheader()
for player in database:
	writer.writerow(database[player])

outfile.close()