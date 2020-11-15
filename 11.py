
def getMem():
	f = open('11.in', 'r')
	text = f.read().split(',')
	array = [int(x) for x in text]
	return array

def checkExtend(array, pos):
	while pos >= len(array):
		array.append(0)
i = 0
relative_i = 0
def run(array, inputs):
	global i, relative_i
	in_pos = 0
	outputs = []
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
			if (array[i] // 10000) % 10 == 2:
				checkExtend(array, relative_i + array[i + 1])
				array[relative_i + array[i + 1]] = inputs[in_pos]
			else:
				array[array[i + 1]] = inputs[in_pos]
			in_pos += 1
			i += 2
		elif array[i] % 100 == 4:
			p1 = getParam(array, i, 1, relative_i)
			outputs.append(p1)
			i += 2
			if len(outputs) == 2:
				return True, outputs
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
			p1 = getParam(array, i, 1, relative_i)
			relative_i += p1
			i += 2
		elif array[i] % 100 == 99:
			break
		else:

			print('Wrong instruction', array[i], i)
			exit(-1)
		
	return False, []

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

running = True
mm = {(0, 0):1}
pos = (0, 0)	# x, y
direction = 0
mem = getMem()
while running:
	curr_color = 0
	if pos in mm:
		curr_color = mm[pos]
	running, outputs = run(mem, [curr_color])
	if not running:
		break
	mm[pos] = outputs[0]
	if direction == 0:
		if outputs[1] == 0:
			pos = (pos[0] - 1, pos[1])
			direction = 1
		elif outputs[1] == 1:
			pos = (pos[0] + 1, pos[1])
			direction = 3
	elif direction == 1:
		if outputs[1] == 0:
			pos = (pos[0], pos[1] - 1)
			direction = 2
		elif outputs[1] == 1:
			pos = (pos[0], pos[1] + 1)
			direction = 0
	elif direction == 2:
		if outputs[1] == 0:
			pos = (pos[0] + 1, pos[1])
			direction = 3
		elif outputs[1] == 1:
			pos = (pos[0] - 1, pos[1])
			direction = 1
	elif direction == 3:
		if outputs[1] == 0:
			pos = (pos[0], pos[1] + 1)
			direction = 0
		elif outputs[1] == 1:
			pos = (pos[0], pos[1] - 1)
			direction = 2


minx = 0
maxx = 0
miny = 0
maxy = 0

for pos in mm:
	if pos[0] > maxx:
		maxx = pos[0]
	if pos[0] < minx:
		minx = pos[0]
	if pos[1] > maxy:
		maxy = pos[1]
	if pos[1] < miny:
		miny = pos[1]
print(minx, maxx)
print(miny, maxy)
for y in range(maxy, miny - 1, -1):
	for x in range(minx, maxx + 1):
		if (x,y) in mm and mm[(x,y)] == 1:
			print("#", end="")
		else:
			print(" ", end="")
	print("")