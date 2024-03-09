# Deleting and renaming files, remove(), rename()
# These two functions must be imported from the os module
# remove('filename') deletes a file
# rename('old name', 'new name') rename old file to new file
# os function directory operations, deleting, moving around, changing things
import os
import time
curDir = os.getcwd() # cwd current working directory
print(curDir) # Displays /Users/jenansaadatmand/Documents
os.mkdir('newDir') # Make new directory 
time.sleep(2) # So we can see the action happening
os.rename('newDir', 'newDir2')  # Rename directory





#time.sleep(2)
#os.rmdir('newDir2') # Remove directory


#rename('myfile.txt', 'nfile.txt')
#file = open(nfile.text)
#print(file)
#file.close()
