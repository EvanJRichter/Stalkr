


class Person:

	def __init__(self, name="John Doe", position="Loser", location="In hiding", industry="Plastics", images=[], contact = "bumpotrungis@gmail.com"):
		self.name = name
		self.position = position
		self.location = location
		self.industry = industry
		self.images = images
		self.contact = contact

	def getName(self):
		return self.name
	def setName(self, name):
		self.name = name

	def getPosition(self):
		return self.position
	def setName(self, position):
		self.positon = position

	def getLocation(self):
		return self.position
	def setLocation(self, position):
		self.position = position

	def getIndustry(self):
		return self.industry
	def setIndustry(self, industry):
		self.industry = industry

	def getImages(self):
		return self.images
	def setImage(self, images):
		self.images = images

	def getContact(self):
		return self.contact
	def setContact(self, contact):
		self.contact = contact
