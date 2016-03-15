class Team():

	def __init__(self,abb,year,roster):
		self.name = abb
		self.abb = abb
		self.year = year
		self.roster = roster

	def __repr__(self):
		return "Team: %s %s" %(self.year,self.name)

	def show_roster(self):
		print("%s %s roster: " %(self.year,self.abb),self.roster)
		return
