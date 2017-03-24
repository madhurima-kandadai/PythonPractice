import sys
from math import log

def convert(s):	
	try:
		return int(s)
	except (ValueError,TypeError) as e:
		print("Conversion Error: {} ".format(str(e)), file = sys.stderr)
	raise #return -1 raise the error instead of returning another value
	
	
def string_log(s):
	v = convert(s)
	return log(v)