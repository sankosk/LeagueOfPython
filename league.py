import urllib, json

class League:
	
	def __init__(self, region):
		self.apiKey = '?api_key=<key>'
		self.genericURL = 'https://%s.api.pvp.net/api/lol/%s/v2.5/league' % (region, region)
		
	def getSummoner(self, sId, entry=True):
		methodPath = '/by-summoner/%s' % sId + self.apiKey
		if sId != '':
			if entry:
				methodPath = '/by-summoner/%s' % sId + '/entry%s' % self.apiKey	
				
			f = urllib.urlopen(self.genericURL+methodPath)
			return json.loads(f.read())
		return "ERROR: May be you forgot write a summoner ID"	
				
	
	def getTeam(self, teamID, entry=True):
		methodPath = '/by-team/%s' % teamID + self.apiKey
		if sId != '':
			if entry:
				methodPath = '/by-team/%s/entry' % teamID + self.apiKey
				
			f = urllib.urlopen(self.genericURL+methodPath)
			if f.read() == '':
				return "The summoner is not member of any team"
				
			return json.loads(f.read())
			
		return "ERROR: May be you forgot write a summoner ID"
	
	def getChallenger(self):
		methodPath = '/challenger%s' % self.apiKey
		f = urllib.urlopen(self.genericURL+methodPath)
		if f.read() == '':
			return "Any challenger, empty"
			
		return json.loads(f.read())
