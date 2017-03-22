#!C:\Users\Madhurima_2\AppData\Local\Programs\Python\Python36-32\Scripts\ python
import sys
from urllib.request import urlopen

def fetch_words(url):
	"""Fetch words from a url"""
	with urlopen(url) as story:
		story_words = []
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
				
	return story_words	
		
def print_items(items):
	for item in items:
		print(item)

def main(url):	 
	words = fetch_words(url) # 'http://sixty-north.com/c/t.txt' use this url
	print_items(words)


if __name__ == "__main__" :
	main(sys.argv[1]) # 0th argument is the module file name. So 1 is used