import urllib, json

class MatchHistory:
	
	def __init__(self):
		self.url = 'https://%s.api.pvp.net/api/lol/%s/v2.2/matchhistory' % (region, region)
		self.apiKey = '?api_key=<key>'

	def getMatchHistory(self, sId):
		if sId != '':
			f = urllib.urlopen(self.url + '/%s%s' % (sId, self.apiKey))
			return json.loads(f.read())
		
		return "ERROR: You must write a valid summoner ID"
