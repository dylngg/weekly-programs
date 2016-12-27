from math import sqrt

class Circle():
	# init
	def __init__(self, radius, ch):
		self.ch = ch
		self.r = radius
		self.text = ''
		
	def __repr__(self):
		return 'Circle()'
		
	def __str__(self):
		return self.text
	
	def create_shape(self):
		radius = self.r
		scale = 4.2
		
		diameter = int(scale * radius)
		radius2 = radius ** 2
		
		# loop through rows
		for row in range(-radius, radius + 1):
			# figure out row length
			length = int(scale * sqrt(radius2 - row ** 2))
			
			row_text = self.ch * length
			self.text = self.text + row_text.center(diameter) + '\n'
		
		return self.text
