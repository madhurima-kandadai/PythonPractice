import time


def modify(k):
	k.append(39) # this changes the argument that is passed to the function
	print("k =", k)
	

def replace(g):
	g = [4,5,6]
	print(g) # value got redefined to another object location instead of changing the same object

	
def replace_contents(g):
	g[0] = 4
	g[1] = 5
	g[2] = 6 # the contents of the arguments will also be modified
	print(g)

	
def banner(message, border='-'):
	line = border * len(message)
	print(line) # border is keyword argument
	print(message)# message string is the positional argument 
	print(line) # banner("hello",border = 'd')


def show_default_time(arg=time.ctime()): # def arguments will be evaluated only once when the function gets executed.
	print(arg) #default arguments gets executed when function gets executed. It has to be changed just like an object
	
def add_spam(menu = []): # the list is created only once. So when it is first executed it has one spam in it. 
	menu.append("spam")#the second time it uses the same object and another spam gets added to it
	return menu
	
	
def add_spam_right_approach(menu = None):
	if menu is None: # use immuable objects in case of default arguments
		menu = []
	menu.append('spam')
	return menu

	
def get_obj_type(obj):
	return type(obj)
	
def add(a,b):
	return a+b
	
