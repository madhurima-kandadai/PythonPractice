count = 0

def show_count():
	print(count)
	

def set_count(c):
	global count
	count = c
	
	
def increment_count():
	global count
	count = count + 1