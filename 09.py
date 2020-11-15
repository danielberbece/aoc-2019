
def getMem():
	f = open('09.in', 'r')
	text = f.read().split(',')
	array = [int(x) for x in text]
	return array

def checkExtend(array, pos):
	while pos >= len(array):
		array.append(0)

def run(array, inputs):
	in_pos = 0
	i = 0
	relative_i = 0
	while True:
		# take instruction
		if array[i] % 100 == 1:
			#add
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			
			checkExtend(array, i + 3)
			checkExtend(array, array[i + 3])
			if (array[i] // 10000) % 10 == 2:
				checkExtend(array,relative_i + array[i + 3])
				array[relative_i + array[i + 3]] = p1 + p2
			else:
				array[array[i + 3]] = p1 + p2
			i += 4
		elif array[i] % 100 == 2:	 # multiply
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			
			checkExtend(array, i + 3)
			checkExtend(array, array[i + 3])
			if (array[i] // 10000) % 10 == 2:
				checkExtend(array,relative_i + array[i + 3])
				array[relative_i + array[i + 3]] = p1 * p2
			else:
				array[array[i + 3]] = p1 * p2
			i += 4
		elif array[i] % 100 == 3:
			checkExtend(array, i + 1)
			checkExtend(array, relative_i + array[i + 1])
			array[relative_i + array[i + 1]] = inputs[in_pos]
			in_pos += 1
			i += 2
		elif array[i] % 100 == 4:
			p1 = getParam(array, i, 1, relative_i)
			print("ouput:", p1)
			i += 2
		elif array[i] % 100 == 5:	# jump if true
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			if p1 != 0:
				i = p2
			else:
				i += 3
		elif array[i] % 100 == 6:	# jump if false
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			if p1 == 0:
				i = p2
			else:
				i += 3			
		elif array[i] % 100 == 7:	# less than
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			store_val = 0
			if p1 < p2:
				store_val = 1
	
			checkExtend(array, i + 3)
			checkExtend(array, array[i + 3])
			if (array[i] // 10000) % 10 == 2:
				array[relative_i + array[i + 3]] = store_val
			else:
				array[array[i + 3]] = store_val
			i += 4			
		elif array[i] % 100 == 8:	# eq
			p1 = getParam(array, i, 1, relative_i)
			p2 = getParam(array, i, 2, relative_i)
			store_val = 0
			if p1 == p2:
				store_val = 1
	
			checkExtend(array, i + 3)
			checkExtend(array, array[i + 3])
			if (array[i] // 10000) % 10 == 2:
				array[relative_i + array[i + 3]] = store_val
			else:
				array[array[i + 3]] = store_val
			i += 4
		elif array[i] % 100 == 9:
			print(i)
			p1 = getParam(array, i, 1, relative_i)
			relative_i += p1
			i += 2
		elif array[i] == 99:
			break
		else:
			print('Wrong instruction', array[i], i)
			exit(-1)
		
	return -1

def getParam(array, i, offset, relative):
	p1 = array[i + offset]
	if (array[i] // ((10 ** offset) * 10)) % 10 == 0:
		if p1 >= len(array):
			p1 = 0
		else:
			p1 = array[p1]
	elif (array[i] // ((10 ** offset) * 10)) % 10 == 2:
		if p1 >= len(array):
			p1 = 0
		else:
			p1 = array[relative + p1]

	return p1

run(getMem(), [1])
run(getMem(), [2])