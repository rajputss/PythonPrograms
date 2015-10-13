class Vehicle:
	
	def __init__(self):
		self.wheels = 4
		self.door = 4
		self.type = "Sedan"

	def calcVelocity(self, x):
		return 3 * x + 10

	def printDetails(self):
		print "Number of doors on my car: " , self.door
		print "Type of my car is: " + self.type
		print "Number of wheels on my car: " , self.wheels
		print "My car runs at a velocity of : " , self.calcVelocity(5)