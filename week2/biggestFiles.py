import os
import sys

print('What dir do you want to look in?')
directory = str(input())

amount = 10
print('Enter how many files you want to see:')
amount = int(input())

# if ignored, put out ten
if amount is '':
    amount = 10

print('Searching', directory,'...')

toptensizes = []
toptensizes.append(0)
topten = []

def search(dir):
    listofdir = os.listdir(dir)
    for item in listofdir:

        if len(toptensizes) > amount:
            del toptensizes[amount:]
            del topten[amount:]

        item = dir + '/' + item
        if os.path.isdir(item):
            search(item)

        else:
            itemsize = os.stat(item).st_size

			# if bigger than last thing in list
            if itemsize > toptensizes[len(toptensizes) - 1]:

				# sort through array to find out where it goes
                for x in range(len(toptensizes)-1, -1, -1):

					# if less than biggest file
                    if itemsize < toptensizes[x]:

						# add file before the larger file
                        toptensizes.insert(x + 1, itemsize)
                        topten.insert(x + 1, item)

						# move on, it's in the right place
                        break

					# if bigger than last file size (biggest size)
                    if itemsize > toptensizes[0]:
						# add file after the largest file
                        toptensizes.insert(0, itemsize)
                        topten.insert(0, item)

						# move on, it's in the right place
                        break

def humanReadableBytes(bit):
    # In MB
    mb = str(bit / 1000000)
    return mb[:4] + ' MB'

def humanReadableString(location):
    # Shorten the long directory name
    return location.replace(directory, '')

search(directory)

print()
print('TOP',amount,'(', directory,'): \n ---------------------')
for x in range(0, len(toptensizes) - 1):
    name = humanReadableString(topten[x])
    size = humanReadableBytes(toptensizes[x])
    output = name + ' is ' + size
    print(output)
