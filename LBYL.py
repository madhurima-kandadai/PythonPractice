import os

p = 'C:/Users/Madhurima_Kandadai/Desktop/PythonPracticeGit/text1.py'

if os.path.exists(p):
	process_file(p) # race condition - the file might get deleted.
else: 
	print('No such file as {}'.format(p)) # directory, garbage