
def getMem():
	f = open('05.in', 'r')
	text = f.read().split(',')
	array = [int(x) for x in text]
	return array

def run(array, in_value):
	i = 0
	while True:
		# take instruction
		if array[i] % 100 == 1:
			#add

			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			p2 = array[i + 2]
			if (array[i] // 1000) % 10 == 0:
				p2 = array[array[i + 2]]

			array[array[i + 3]] = p1 + p2
			i += 4
		elif array[i] % 100 == 2:	 # multiply
			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			p2 = array[i + 2]
			if (array[i] // 1000) % 10 == 0:
				p2= array[array[i + 2]]

			array[array[i + 3]] = p1 * p2
			i += 4
		elif array[i] % 100 == 3:
			array[array[i + 1]] = in_value
			i += 2
		elif array[i] % 100 == 4:
			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			print("ouput:", p1, i)
			i += 2
		elif array[i] % 100 == 5:	# jump if true
			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			p2 = array[i + 2]
			if (array[i] // 1000) % 10 == 0:
				p2= array[array[i + 2]]
			if p1 != 0:
				i = p2
			else:
				i += 3
		elif array[i] % 100 == 6:	# jump if false
			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			p2 = array[i + 2]
			if (array[i] // 1000) % 10 == 0:
				p2= array[array[i + 2]]
			if p1 == 0:
				i = p2
			else:
				i += 3			
		elif array[i] % 100 == 7:	# less than
			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			p2 = array[i + 2]
			if (array[i] // 1000) % 10 == 0:
				p2= array[array[i + 2]]
			store_val = 0
			if p1 < p2:
				store_val = 1
	
			array[array[i + 3]] = store_val
			i += 4			
		elif array[i] % 100 == 8:	# eq
			p1 = array[i + 1]
			if (array[i] // 100) % 10 == 0:
				p1 = array[array[i + 1]]
			p2 = array[i + 2]
			if (array[i] // 1000) % 10 == 0:
				p2= array[array[i + 2]]
			store_val = 0
			if p1 == p2:
				store_val = 1
	
			array[array[i + 3]] = store_val
			i += 4			
		elif array[i] == 99:
			break
		else:
			print('Wrong instruction', array[i], i)
			exit(-1)
		
	return array[0]


# part 1
print('part 1:', run(getMem(), 1))
# part 2
print('part 2', run(getMem(), 5))
