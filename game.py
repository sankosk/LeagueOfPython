import urllib, json

class Game:
	
	def __init__(self, region):
		self.apiKey = '?api_key=<key>'
		self.url = 'https://%s.api.pvp.net/api/lol/%s/v1.3/game/by-summoner/' % (region, region)

	def getGame(self, sId=''):
		if sId != '':
			f = urllib.urlopen(self.url+'%s/recent%s' % (sId, self.apiKey))
			return json.loads(f.read())
		
		return "ERROR: You have to write a summoner ID"

	def showGame(self, sId=''):
		try:
			content = self.getGame(sId)
			return content
		except:
			return "ERROR: May be you didnt write a summoner ID or you write a not valid ID"
		
print Game('euw').showGame('34621210')
