import tree
import argparse
import sys

def main(args):
	# get input for tree width and height
	parser = argparse.ArgumentParser(description='Create a Cirstmas Tree made of text')
	parser.add_argument('-y','--height', help='Input for the height of the tree',required=True)
	parser.add_argument('-x','--width', help='Input for the width of the tree',required=True)
	parser.add_argument('-c','--char', help='Input for the character of the tree',required=True)
	parser.add_argument('-o','--ornament', help='Input for the ornament character',required=False)
	args = parser.parse_args()
	
	height = int(args.height)
	width = int(args.width)
	ch = str(args.char)
	ornament = str(args.ornament)
	
	if len(ornament) is not 1:
		ornament = 'o'
		print('no ornaments')
	
	if len(ch) > 1:
		print('Error: Character input is longer than 1 character')
		sys.exit()
	
	cirstmas_tree = tree.Tree(height, width, ch, ornament)
	cirstmas_tree.create_tree()
	print(cirstmas_tree)
	
if __name__ == "__main__":
	sys.exit(main(sys.argv))
