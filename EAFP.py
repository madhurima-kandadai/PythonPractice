import os

p = 'C:/Users/Madhurima_Kandadai/Desktop/PythonPracticeGit/text1.py'

try:
	process_file(f)
except OSError as e: # this covers all the major errors 
	print('Could not process file becaues {}'.format(str(e)))