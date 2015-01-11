import urllib, json

class Stats:
	
	def __init__(self, region):
		self.url = 'https://%s.api.pvp.net/api/lol/%s/v1.3/stats/by-summoner/' % (region, region)
		self.apiKey = '?api_key=<key>'
		
	def getRanked(self, sId):
		if sId != '':
			methodPath = '%s/ranked%s' % (sId, self.apiKey)
			f = urllib.urlopen(self.url+methodPath)
			return json.loads(f.read())
		
		return "ERROR: You must write a summoner ID"
		
	def getSummary(self, sId):
		if sId != '':
			methodPath = '%s/summary%s' % (sId, self.apiKey)
			f = urllib.urlopen(self.url+methodPath)
			return json.loads(f.read())
		
		return "ERROR: You must write a summoner ID"
