import time
#from pprint import pprint as pp

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
	
	
def enumerate_example(): # to create tuples
	t = [6, 372, 8862, 148800, 2096886]
	for p in enumerate(t):
		print(p)
	for (i,v) in enumerate(t):
		print("i = {} , v = {}".format(i,v))
		
def wrong_iteration():
	t = [1,2,3,4,5] # should not iterate like this through lists
	for p in range(len(t)):
		print(t[p])
		

def correct_iteration():
	t = [1,2,3,4,5] # this is the correct way of iterating lists
	for p in t:
		print(p)
		
		
def string_list():
	str = "show how to index into sequences".split()
	print(str)
	print(str[1:4]) # for 1 to 3 elements
	print(str[3:]) #for 3 to last
	print(str[:3] + str[4:]) # omit element at 3
	
def copy_list():
	s = [1,2,3,4]
	new_list = s[:] # copying a list to another object
	
def list_slicing_shallow_copy():
		a = [[1,2], [3,4]]
		b = a[:] # the copy is a shallow copy - only the top level list is duplicated and is assigned to b 
		a[1][1] = 25 # the same value is assigned to b too as the copy is shallow
		print(a)
		print(b)
		
		
def delete_from_list():
	u = ['a','b','c','d','e']
	del u[3]
	u.remove('c')
	del u[u.index('e')]
	

def insert_into_list():
		a = "I accidentally the whole universe".split()
		print(a)
		a.insert(2, 'destroyed')
		print(a)
		
		
def list_concat():
	a = [1,2,3]
	print(a)
	b = [4,5,6]
	print(b)
	c = a + b
	print(c)
	c += [18,19,20]
	print(c)
	c.extend([76,129])
	
	
def reverse_sort():
	a = [1,22,3,6,7,00,1323]
	a.reverse()
	a.sort()
	a.sort(reverse=True) # print descending order
	
def keyparam_list_sort():
	h = "not perplexing do handwriting family where I illegibly know doctors U"
	h.sort(key=len)
	print(h)
	
def sorted_reversed():
	x = [4,9,2,1]
	y = sorted(x)
	print(x)
	print(y)
	p = [9,3,1,0]
	q = p.reversed()
	print(p)
	print(list(q)) # need list constructor to evaluate the value of reversed
	
	
def tuple_to_dict():
		names_ages = {('Alice', 32), ('Bob', 48), ('Charlie', 28), ('Daniel', 33)}
		d = dict(names_ages)
		print(d)
		
def dict_copy_update():
	f = {'indigo':491530, 'seashell':16774638, 'goldenrod':14329120}
	g = dict(wheat=0xF5DEB3, khaki=0xF0E68C, crimson=0xDC143C)
	a = f.copy() # copying 
	b = dict(f) # copying
	f.update(g) # update from one dictionary. If the values are already present, the values from target are updated in the sourcr
	print(f)
	print(g)
	print(a)
	print(b)
	for key in f:
		print("{key}=>{value}".format(key=key, value=f[key]))
	for value in f.values(): # this prints only values f.keys() for printing only keys
		print(value)
	for key,value in f.items(): # for printing the key value pairs
		print("key is {} and value is {}".format(key,value))
		
		
def dict_membership_testing():
	f = {'indigo':491530, 'seashell':16774638, 'goldenrod':14329120}
	print('indigo' in f)
	print('indigo' not in f)
	
	
def dict_delete():
	f = {'indigo': 491530, 'seashell': 16774638, 'goldenrod': 14329120, 'wheat': 16113331, 'khaki': 15787660, 'crimson': 14423100}
	print(f)
	del f['indigo']
	print(f)
	#print(pp(f))  pprint usage
	
	
def set_examples():
	p = {6,28,496,8128,33550336}
	print(p) # each is an independent object
	d = set() # creating an empty set will not accept duplicates
	d = {81, 108}
	print(81 in d)
	print(81 not in d)
	d.add(12)
	d.add(108) # will not produce any duplicates
	d.update([37,128,97]) # can be updated
	#d.remove(98) throws error of element is not there
	d.discard(98) # will not throw error if the item is not available
	a = d.copy() #shallow copy
	
	
def set_functions():
		blue_eyes = {'Olivia', 'Harry', 'Lily', 'Jack', 'Amelia'}
		blonde_hair = {'Harry', 'Jack', 'Amelia', 'Mia', 'Joshua'}
		smell_hcn = {'Harry', 'Amelia'}
		taste_pcn = {'Harry', 'Lily', 'Amelia', 'Lola'}
		o_blood = {'Mia', 'Joshua', 'Lily', 'Olivia'}
		b_blood = {'Amelia', 'Jack'}
		a_blood = {'Harry'}
		ab_blood = {'Joshua', 'Lola'}
		#blonde_hair or blue_eyes or both -- union operator
		print('blonde_hair or blue_eyes', blonde_hair.union(blue_eyes)) # commutative
		print('blonde_hair and blue_eyes', blonde_hair.intersection(blue_eyes)) #commutative
		print('blonde_hair without blue_eyes', blonde_hair.difference(blue_eyes))  ## non commutative
		print('blonde_hair or blue_eyes but no both', blonde_hair.symmetric_difference(blue_eyes)) #commutative
		print('Smell hcn also have blonde_hair ',smell_hcn.issubset(blonde_hair))
		print('taste_pcn also smell_hcn # superset', taste_pcn.issuperset(smell_hcn))
		print('two sets have nothing in common', a_blood.isdisjoint(b_blood))