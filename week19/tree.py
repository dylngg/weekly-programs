import math
import random

class Tree():
	# init
	def __init__(self, height, width, ch, ornament = '*'):
		self.height = height
		
		self.width = width
		if width % 2 is not 0:
			sefl.width += 1
		
		self.tree = ''
		self.tree_ratio = (self.width / 2.0) / self.height
		self.ch = ch
		self.ornament = ornament
	
	
	def __repr__(self):
		return 'Tree()'
	
	
	def __str__(self):
		return self.tree
	
	
	'''
	Creates a text based tree and returns the tree text
	'''
	def create_tree(self):
		tree_top = self.create_top()
		tree = self.create_stump(tree_top)
		self.tree = tree
		
		return self.tree
		
	
	'''
	Creates the top part of the tree(the triangle)
	'''
	def create_top(self):
		tree = ''
		for x in range(1, self.height):
			# use slope of tringle to figure out length of half the triangle, then subtract to get space
			l_fill = int(self.tree_ratio * x)
			l_spacing = int(self.width / 2) - l_fill
			r_fill = l_fill - 1
			r_spacing = int(self.width / 2) - r_fill
			
			ornament = random.randint(0, self.width)
			
			# add all the parts of the row to the tree line
			tree += ''.join([' ' for x in range(0, l_spacing)])
			tree += ''.join([self.ch if x is not ornament else self.ornament for x in range(0, l_fill)])
			tree += ''.join([self.ch if x is not ornament else self.ornament for x in range(0, r_fill)])
			tree += ''.join([' ' for x in range(0, r_spacing)])
			
			tree += '\n'
		
		return tree
	
	
	'''
	Creates the stump part of the tree
	'''
	def create_stump(self, tree_top):
		tree = tree_top
		stump = math.floor((1/6.0) * self.width)
		stump_spacing = math.ceil((self.width - stump) / 2) - 1
		tree += ''.join([' ' for x in range(0, int(stump_spacing))])
		tree += ''.join(['I' for x in range(0, int(stump))])
		tree += ''.join([' ' for x in range(0, int(stump_spacing))])
		
		return tree
