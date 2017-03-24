def convert(s):	
	try:
		return int(s)
	except (ValueError,TypeError):
		pass		
	return -1