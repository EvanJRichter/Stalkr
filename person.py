


class Person:

	def __init__(self, name="John Doe", position="Loser", location="In hiding", industry="Plastics", image="<image src =\"http://upload.wikimedia.org/wikipedia/en/c/c8/CarterIII.jpg\"/>"):
		self.name = name
		self.position = position
		self.location = location
		self.industry = industry
		self.image = image

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

	def getImage(self):
		return self.image
	def setImage(self, image):
		self.image = image

