import zipfile
import os

def backupZipDir():
	directory = str(input('What directory do you want to look for folders to zip up?'))
	
	zipFilename = str(input('What do you want to name the zip file?'))
	if '.zip' not in zipFilename:
		zipFilename = zipFilename + '.zip'
	
	zipDestination = str(input('Where do you want the zip file to end up?'))
	
	# create the zip file
	print('Creating %s...' % (zipFilename))
	backupZip = zipfile.ZipFile(zipFilename, 'w')

	# walk the entire directory tree and compress the files in each directory.
	for directoryname, subdirectorys, filenames in os.walk(directory):
		if directoryname is not directory:
			directoryname.replace(directory, '')
		print(directoryname, subdirectorys, filenames)
		print('Adding files in %s...' % (directoryname))
		# add the current directory to the ZIP file.
		backupZip.write(directoryname)

		# add all the files in this directory to the ZIP file.
		for filename in filenames:
			backupZip.write(os.path.join(directoryname, filename))
	backupZip.close()
	
	os.rename(os.getcwd() + '/' + zipFilename, zipDestination + '/' + zipFilename)
	print('Done.')

backupZipDir()

