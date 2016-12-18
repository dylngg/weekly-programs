import circle
import argparse
import sys

def main(args):
	# get input for circle
	parser = argparse.ArgumentParser(description='Create a circle of text')
	parser.add_argument('-r','--radius', help='Input for the readius of the circle',required=True)
	parser.add_argument('-c','--char', help='Input for the text characters of the circle',required=False)
	args = parser.parse_args()
	
	radius = int(args.radius)
	ch = str(args.char)
	
	if ch is None:
		ch = '*'
	
	if len(ch) > 1:
		print('Error: Character input is longer than 1 character')
		sys.exit()
	
	c1 = circle.Circle(radius, ch)
	c1.create_shape()
	print(c1)
	
if __name__ == "__main__":
	sys.exit(main(sys.argv))
