import sys

def sqrt(x):
	if x < 0:
		raise ValueError("Cannot compute square root of negative number {}".format(x))
	guess = x
	i = 0
	while guess * guess != x and i < 20:
		guess = (guess + x / guess) / 2.0
		i += 1
	return guess
	
	
def main():
	try:
		print(sqrt(9))		
		print(sqrt(2))
		print(sqrt(-1))
		print(sqrt({1,2,3}))
		print("This is never printed")
	except ZeroDivisionError:
		print("Cannot compute square root of negative number.")
	except TypeError:
		print("The argument should be of integer type.")
	except ValueError as e:
		print(e, file = sys.stderr)
	print("Program execution continues normally here.")
	
	
if __name__ == '__main__':
	main()