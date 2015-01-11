import urllib, json

class Champion:
	
	def __init__(self, region):
		self.apiKey = '?api_key=<key>'
		self.url = 'https://%s.api.pvp.net/api/lol/%s/v1.2/champion' % (region, region)
		
	def getChampion(self, sId=''):
		if sId != '':
			f = urllib.urlopen(self.url+'/%s' % (sId + self.apiKey))
			return json.loads(f.read())
		
		f = urllib.urlopen(self.url + self.apiKey)
		return json.loads(f.read())

print Champion('euw').getChampion()
