from tkinter import Tk
import sys

def main(args):
	# tkinter setup
	root = Tk()
	root.withdraw()
	
	try:
		# capture clipboard
		clipboardItems = []
		while True:
			# make sure it is text
			try:
				clipboard = root.selection_get(selection="CLIPBOARD")
				
				# make sure it is not previously in list
				if clipboard not in clipboardItems:
					# add to list
					clipboardItems.append(clipboard)
				
			except:
				pass
	
	except (KeyboardInterrupt, SystemExit):
		print('Saving...')
		txtFile = open("clipboard.txt", "w")
		txtFile.write("\n".join(str(x) for x in clipboardItems))
		txtFile.close()
		sys.exit()
		
if __name__ == '__main__':
    sys.exit(main(sys.argv))
