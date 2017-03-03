import os
import sys
import random
import shutil

def main(args):
	directory = str(input('What directory do you want me to mess up?: '))
	movingCount = int(input('How many files do you want to mess up?: '))
	
	# repeat however many times
	for x in range(0,movingCount):
		# recheck dir
		files = getFiles(directory)
		directories = getDir(directory)
		
		moveRandomFile(directories, files)
		
	print('Mission Accomplished.')
	
def getFiles(directory):
	files = []
	
	for folderName, subfolders, filenames in os.walk(directory):
		subfolders[:] = [d for d in subfolders if not d.startswith('.')] 
		
		for filename in filenames:
			files.append(str(os.path.join(folderName, filename)))

	return files

def getDir(directory):
	directories = []
	
	for folderName, subfolders, filenames in os.walk(directory):
		subfolders[:] = [d for d in subfolders if not d.startswith('.')] 
		directories.append(folderName)
	
	return directories
	
def moveRandomFile(directories, files):
	fileToMove = files[random.randint(0,len(files) - 1)]
	destination = directories[random.randint(0,len(directories) - 1)]
	if os.path.dirname(destination) is not os.path.dirname(fileToMove):
		print('Moving', fileToMove, 'to', destination)
		shutil.move(fileToMove, destination)
		
if __name__ == '__main__':
    sys.exit(main(sys.argv))
