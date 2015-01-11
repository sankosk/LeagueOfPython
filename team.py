import urllib, json

class Team:
	
	def __init__(self):
		self.url = 'https://%s.api.pvp.net/api/lol/%s/v2.4/team' % (region, region)
		self.apiKey = '?api_key=<key>'
		
	def getTeamBySummoner(self, sId):
		if sId != '':
			f = urllib.urlopen(self.url + '/by-summoner/%s%s' % (sId, self.apiKey))
			return json.loads(f.read())
		
		return "ERROR: You must to write a summoner ID"
	
	def getTeamByID(self, sId):
		if sId != '':
			f = urllib.urlopen(self.url + '/%s%s' % (sId, self.apiKey))
			return json.loads(f.read())
		
		return "ERROR: You must to write a summoner ID"
