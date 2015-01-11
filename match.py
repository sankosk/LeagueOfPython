import urllib, json

class Match:
	
	def __init__(self, region):
		self.url = 'https://%s.api.pvp.net/api/lol/%s/v1.2/match' % (region, region)
		self.apiKey = '?api_key=<key>'
		
	def getMatch(self, sId):
		if sId != '':
			f = urllib.urlopen(self.url+'/%s%s' % (sId, self.apiKey))
			return json.loads(f.read())
		
		return "ERROR: You must to write a match ID"

