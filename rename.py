import os
import shutil
import re

dir = 'C:/Users/dylan/Dropbox/weekly-programs'
for fileName in os.listdir(dir):
    # week + num (week5) if num is less than 10 and doesn't have a 0 in front 	
    if len(fileName[4:]) < 2 and '0' not in  fileName[4:]:
        os.rename(os.path.join(dir, fileName), os.path.join(dir, fileName[:4] + '0' + fileName[4:]))
