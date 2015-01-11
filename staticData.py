import urllib, json

class LoLStaticData:
	
	def __init__(self, region):
		self.url = 'https://global.api.pvp.net/api/lol/static-data/%s/v1.2' % region
		self.apiKey = '?api_key=<key>'

	def getChampion(self, sId=''):
		methodPath = '/champion%s' % self.apiKey
		if sId != '':
			methodPath = '/champion/%s%s' % (sId, self.apiKey)
		
		f = urllib.urlopen(self.url+methodPath)
		return json.loads(f.read())

	
	def getItem(self, sId):
		methodPath = '/item%s' % self.apiKey
		if sId != '':
			methodPath = '/item/%s%s' % (sId, self.apiKey)
			
		f = urllib.urlopen(self.url+methodPath)
		return json.loads(f.read())
		
	def getLanguages(self):
		f = urllib.urlopen(self.url+'/languages%s'%self.apiKey)
		return json.loads(f.read())

	
	def getMasteries(self, sId=''):
		methodPath = '/mastery%s' % self.apiKey
		if sId != '':
			methodPath = '/mastery/%s%s' %(sId, self.apiKey)
			
		f = urllib.urlopen(self.url+methodPath)
		return json.loads(f.read())
	
	def getRealm(self):
		f = urllib.urlopen(self.url+'/realm%s' % self.apiKey)
		return json.loads(f.read())
	
	def getRune(self, sId=''):
		methodPath = '/rune%s' % self.apiKey
		if sId != '':
			methodPath = '/rune/%s%s' % (sId, self.apiKey)
			
		f = urllib.urlopen(self.url + methodPath)
		try:
			return json.loads(f.read())
		except:
			return "ERROR: May be you write an invalid rune ID"
	
	def getSpell(self, sId=''):
		methodPath = '/summoner-spell%s' % self.apiKey
		if sId != '':
			methodPath = '/summoner-spell/%s%s' % (sId, self.apiKey)
			
		f = urllib.urlopen(self.url + methodPath)
		try:
			return json.loads(f.read())
		except:
			return "ERROR: May be you write and invalid rune ID"
	
	def getVersions(self):
		f = urllib.urlopen(self.url+'/versions%s'%self.apiKey)
		return json.loads(f.read())
			
