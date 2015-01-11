import urllib, json

class Summoner:
	
	def __init__(self, region):
		self.url = 'https://%s.api.pvp.net/api/lol/%s/v1.3/stats/by-summoner/' % (region, region)
		self.apiKey = '?api_key=<key>'
		
	def getSummonerName(self, sId):
		if sId != '':
			f = urllib.urlopen(self.url + '/by-name/%s%s' % (sId, self.apiKey))
			return json.loads(f.read())
		
		return "ERROR: You must to write a summoner ID"

	def getSummonerInfo(self, sId):
		if sId != '':
			f = urllib.urlopen(self.url + '/%s%s' % (sId, self.apiKey))
			return json.loads(f.read())
		
		return "ERROR: You must to write a summoner ID"

	def getMasteries(self, sId):
		if sId != '':
			f = urllib.urlopen(self.url + '/masteries/%s%s' % (sId, self.apiKey))
			return json.loads(f.read())
		
		return "ERROR: You must to write a summoner ID"

	def getName(self, sId):
		if sId != '':
			f = urllib.urlopen(self.url + '/name/%s%s' % (sId, self.apiKey))
			return json.loads(f.read())
		
		return "ERROR: You must to write a summoner ID"

	def getRunes(self, sId):
		if sId != '':
			f = urllib.urlopen(self.url + '/runes/%s%s' % (sId, self.apiKey))
			return json.loads(f.read())
		
		return "ERROR: You must to write a summoner ID"
