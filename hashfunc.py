def code(a):
	l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	new_a = ''
	for x in a:
		if x.isdigit():
			if x == '7':
				new_a += '#'
			elif x == '2':
				new_a += '$'
			else:
				new_a += str(9 - int(x))
		else:
			if l.index(x) < 13:
				new_a += l[26 - l.index(x)].upper()
			else:
				new_a += l[26 - l.index(x)].lower()
	return new_a
def decode(new_a):
	l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
	a = ''
	for x in new_a:
		if x == '#':
			a += '7'
		elif x == '$':
			a += '2'
		elif x.isdigit():
			a += str(9 - int(x))
		else:
			if x.upper() == x:
				a += l[26 - l.index(x.lower())]
			else:
				a += l[26 - l.index(x.lower())]
	return a
