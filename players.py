from decimal import *

class Player():

	def __init__(self,firstname,lastname,team='',position=''):
		self.firstname = firstname
		self.lastname = lastname
		self.name = "%s %s" %(firstname,lastname)
		self.position = position
		self.team = team

	def __repr__(self):
		return "Player: %s %s, %s, %s" % (self.firstname,self.lastname,self.position,self.team)

	def displaySeasons(self):
		if not self.seasons:
			return ("No seasons found for player: ", self.name)
		else:
			print(self.seasons.keys())
			for i in self.seasons.keys():
				print(self.seasons[i])	

class BatterSeason():

	def __init__(self,player,year,team='',age=0,pa=0,ab=0,hits=0,bb=0,hr=0,runs=0,rbi=0,sb=0):
		self.player,self.team = player,team
		self.year,self.age,self.pa,self.ab,self.hits,self.bb = year,age,pa,ab,hits,bb
		self.hr,self.runs,self.rbi,self.sb = hr,runs,rbi,sb
		try: self.avg = format(round(hits/ab,3), '.3f')
		except: self.avg = format(0, '.3f')
		try: self.obp = format(round((hits+bb)/pa,3), '.3f')
		except: self.obp = format(0, '.3f')


	def __repr__(self):
		return ("Player: %s | Season: %s | PA: %d | AB: %d | H: %d | BB: %d | HR: %d | R: %d | RBI: %d | SB: %d | AVG: %s | OBP: %s"
				% (self.player,self.year,self.pa,self.ab,self.hits,self.bb,self.hr,self.runs,self.rbi,self.sb,self.avg,self.obp))

	def exportSeason(self):
		return [self.player.name, self.team, self.age, self.pa, self.ab, self.hits, self.bb, 
		self.hr, self.runs, self.rbi, self.sb, self.avg, self.obp]


class PitcherSeason():

	def __init__(self,player,year,team='',age=0,g=0,gs=0,w=0,l=0,ip=0,sv=0,hits=0,bb=0,so=0,er=0):
		self.player,self.team = player,team
		self.year,self.age,self.g,self.gs,self.wins,self.losses = year,age,g,gs,w,l
		self.sv,self.hits,self.bb,self.so,self.er = sv,hits,bb,so,er
		self.ip = (ip + 2.3 *(ip % 1))
		try:
			self.era = format(round(9*er/ip,2), '.2f')
			self.whip = format(round((hits+bb)/ip,2), '.2f')
			self.soper9 = format(round(9*(so/ip),2), '.2f')
			self.bbper9 = format(round(9*(bb/ip),2), '.2f')
		except:
			self.era,self.whip,self.soper0,self.bbper9 = [format(0, '.2f')]*4


	def __repr__(self):
		return ("Player: %s | Season: %s | G: %d | W-L: %d-%d | IP: %d | SV: %d | H: %d | ERA: %s | WHIP: %s | SO/9: %s | BB/9: %s" 
				% (self.player,self.year,self.g,self.wins,self.losses,self.ip,self.sv,self.hits,self.era,self.whip,self.soper9,self.bbper9))

	def exportSeason(self):
		return [self.player.name, self.team, self.age, self.g, self.gs, self.wins, self.losses, 
		self.ip, self.sv, self.hits, self.bb, self.so, self.era, self.whip]